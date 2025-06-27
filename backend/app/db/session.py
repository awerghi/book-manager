from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL_ENDPOINT = "sqlite:///./bookstore.db"
engine = create_engine(DB_URL_ENDPOINT,connect_args={'check_same_thread' : False})
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)


Base = declarative_base()