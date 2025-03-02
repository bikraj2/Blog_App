from datetime import datetime
from typing import Annotated
from fastapi import HTTPException, Query, Depends, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from sqlmodel import asc, func, select
from ..models.models import *
from ..dependecies import SessionDep
from ..core.auth import get_current_active_user

router = APIRouter(prefix="/blogs", tags=["blogs"])

@router.post("", response_model=BlogPublic)
def create_blog(
    blog: BlogCreate,
    session: SessionDep,
    current_user: User = Depends(get_current_active_user)):
    blog.author_id = current_user.id 
    db_blog = Blog.model_validate(blog)
    session.add(db_blog)
    session.commit()
    session.refresh(db_blog)
    return db_blog


@router.get("", response_model=list[BlogPublic])
def read_blogs(
    session: SessionDep,
    offset: int = 0,
    limit: int = 10,
):
    total_count = session.exec(select(func.count()).select_from(Blog)).one()

    blogs_query = select(Blog).order_by(Blog.created_at.desc()).offset(offset).limit(limit)
    blogs = session.exec(blogs_query).all()

    # Convert datetime fields to ISO format before returning response
    serialized_blogs = [
        {
            **blog.model_dump(),
            "created_at": blog.created_at.isoformat() if isinstance(blog.created_at, datetime) else blog.created_at
        }
        for blog in blogs
    ]

    return JSONResponse(
        content= {
            "data": serialized_blogs,
            "total_count" :total_count
        },
    )
@router.get("/{blog_id}", response_model=Blog)
def read_blog(blog_id: int, session: SessionDep):
    blog = session.get(Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.patch("/{blog_id}", response_model=BlogPublic)
def update_blog(
    blog_id: int,
    blog: BlogUpdate,
    session: SessionDep,
    current_user: User = Depends(get_current_active_user),  # Require authentication
):
    blog_db = session.get(Blog, blog_id)
    if not blog_db:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog_db.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this blog")

    blog_data = blog.model_dump(exclude_unset=True)
    
    # Check for version conflict
    if blog_db.version != blog_data.get("version", blog_db.version):
        raise HTTPException(status_code=409, detail="Version mismatch! Someone else modified this blog.")

    blog_data["version"] += 1

    for key, value in blog_data.items():
        setattr(blog_db, key, value)

    session.commit()
    session.refresh(blog_db)
    return blog_db


@router.delete("/{blog_id}")

def delete_blog(
    blog_id: int,
    session: SessionDep,
    current_user: User = Depends(get_current_active_user),  
):
    blog = session.get(Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this blog")

    session.delete(blog)
    session.commit()
    return {"message": "Blog deleted successfully"}
