from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DB_URL_ENDPOINT = "sqlite:///./bookstore.db"
engine = create_engine(DB_URL_ENDPOINT,connect_args={'check_same_thread' : False})
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():

    db = session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


Base = declarative_base()