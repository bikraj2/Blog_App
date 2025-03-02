from contextlib import asynccontextmanager
from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware
from ..app.dependecies import SessionDep

from .core.db import init_db
from .routes import users,blogs

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(SessionDep)
    yield
app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(blogs.router)
app.include_router(users.router)


## Add this middleware if you have configured your browser to accept a https secure server with sefl signed certificate
# @app.middleware("http")
# async def add_csp_header(request, call_next):
#     response = await call_next(request)
#     response.headers["Content-Security-Policy"] = (
#         "default-src 'self'; "  
#         "script-src 'self' 'unsafe-inline'; "
#         "style-src 'self' 'unsafe-inline'; "
#         "img-src 'self' data:; "  
#         "frame-src 'none'; "  
#     )
#     return response

