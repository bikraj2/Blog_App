from sqlmodel import SQLModel, Session, create_engine  

from .configs import settings

engine = create_engine(str( settings.SQLALCHEMY_DATABASE_URI))
def init_db(session: Session) -> None:
    SQLModel.metadata.create_all(engine)

