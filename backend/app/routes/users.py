from datetime import timedelta
from typing import Annotated 


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from ..core.configs import settings
from ..models.models import User, UserCreate, UserPublic,Token
from ..dependecies import  SessionDep

from ..core.auth import *

router = APIRouter(prefix="/users", tags=["users"])





# Register a new user
@router.post("/register", response_model=UserPublic)
def register_user(user_data: UserCreate, db: SessionDep):
    existing_user = get_user(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    existing_user = get_user_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")


    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, full_name=user_data.full_name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Login user and return access token
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:  SessionDep):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")


