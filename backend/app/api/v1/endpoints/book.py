from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status

from app.db.session import session
from app.db.models import Book
from app.api.v1.endpoints.models.book_model import BookModel
from app.core.exception import BookNotFoundException

router = APIRouter(
    prefix="/api/v1",
    tags=["Operations"]
)

def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/library/books",status_code=status.HTTP_200_OK)
async def get_all_books (db : db_dependency):
    return db.query(Book).all()

@router.post("/library/add-book",status_code=status.HTTP_201_CREATED)
async def add_book_to_bookstore(db : db_dependency, book_info : BookModel):
    book_model = Book(**book_info.model_dump())
    db.add(book_model)
    db.commit()

@router.put ("/library/update-book",status_code=status.HTTP_204_NO_CONTENT)
async def update_library_book (db : db_dependency , book_updated_info : BookModel):
    library_book = db.query(Book).filter(Book.id == book_updated_info.id).first()
    if library_book is None:
        raise BookNotFoundException()

    library_book.title = book_updated_info.title
    library_book.subtitle = book_updated_info.subtitle
    library_book.isbn_10 = book_updated_info.isbn_10
    library_book.isbn_13 = book_updated_info.isbn_13
    library_book.language = book_updated_info.language
    library_book.edition = book_updated_info.edition
    library_book.publication_date = book_updated_info.publication_date

    db.add(library_book)
    db.commit()


@router.delete("/library/book/remove",status_code=status.HTTP_204_NO_CONTENT)
async def remove_book_from_library (db : db_dependency, book_id_to_remove : int = Query(gt=0)):
    library_book = db.query(Book).filter(Book.id == book_id_to_remove).first()

    if library_book is None:
        raise BookNotFoundException()
    db.query(Book).filter(Book.id == book_id_to_remove).delete()
    db.commit()





