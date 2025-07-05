from app.db.session import Base
from sqlalchemy import Column, INTEGER, String, ForeignKey
from app.db.session import engine


class Book(Base):


    __tablename__ = "Book"

    title = Column(String)
    subtitle = Column(String)
    isbn_10 = Column(String)
    isbn_13 = Column(String,primary_key=True,unique=True)
    language = Column(String)
    edition = Column(String)
    publication_date = Column(String)
    author_id     = Column(INTEGER)

class Author(Base):

    __tablename__ = "author"

    id = Column(INTEGER,primary_key=True)
    name = Column(String)
    number_of_published_books = Column(INTEGER)




Base.metadata.create_all(bind=engine)