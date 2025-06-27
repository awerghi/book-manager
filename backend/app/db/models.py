from app.db.session import Base
from sqlalchemy import Column, INTEGER, String
from app.db.session import engine


class Book(Base):


    __tablename__ = "Book"

    id = Column(INTEGER,primary_key=True)
    title = Column(String)
    subtitle = Column(String)
    isbn_10 = Column(String)
    isbn_13 = Column(String)
    language = Column(String)
    edition = Column(String)
    publication_date = Column(String)




Base.metadata.create_all(bind=engine)