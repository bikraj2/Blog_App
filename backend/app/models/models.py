
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from enum import Enum
import bleach

# Define an Enum for categories with a limited set of values
class CategoryEnum(str, Enum):
    TECH = "Tech"
    LIFESTYLE = "Lifestyle"
    BUSINESS = "Business"
    EDUCATION = "Education"
    ENTERTAINMENT = "Entertainment"

# Define a function to clean HTML content
def clean_html(content: str) -> str:
    # Allowed tags (can be customized)
    allowed_tags = ['b', 'i', 'u', 'strong', 'em', 'p', 'a', 'h1', 'h2', 'h3', 'ul', 'li', 'ol', 'blockquote']
    cleaned_content = bleach.clean(content, tags=allowed_tags, strip=True)
    return cleaned_content

class BlogBase(SQLModel):
    title: str = Field(index=True)
    content: str = Field()
    read_time: int = Field()
    category: CategoryEnum = Field(default=CategoryEnum.TECH)  # Default to 'TECH'
    # Clean the content before creating or updating the blog
    def clean_content(self):
        self.content = clean_html(self.content)

class Blog(BlogBase, table=True):
    id: int | None  = Field(default = None,primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    version: int = Field(default=1)



    category: CategoryEnum | None = None  # category can now be updated with one of the enum values
    author_id: int = Field(foreign_key="user.id")
    # Override the model save method to clean content before saving
    def save(self, session):
        self.clean_content()
        session.add(self)
        session.commit()
        session.refresh(self)

class BlogPublic(BlogBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    version: int = Field(default=1)
class BlogCreate(BlogBase):
    author_id: str |None = None
    pass


class BlogUpdate(BlogBase):
    title: str | None = None
    content: str | None = None
    read_time: int | None = None
    category: CategoryEnum | None = None  # category can now be updated with one of the enum values
    version: int

    # Clean the content before updating
    def clean_content(self):
        if self.content:
            self.content = clean_html(self.content)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: Optional[str] = Field(default=None, unique=True)
    full_name: Optional[str] = Field(default=None)

class User(UserBase, table=True):
    id :int= Field(index=True, primary_key=True)
    hashed_password: str

class UserPublic(UserBase):
    id: int

class UserCreate(UserBase):
    password: str  # Plain text password before hashing

class UserUpdate(SQLModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


