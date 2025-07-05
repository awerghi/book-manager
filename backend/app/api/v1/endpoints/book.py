from fastapi import APIRouter, HTTPException, Query
from starlette import status
from prometheus_client import Counter


from app.db.session import session
from app.db.models import Book, Author
from app.api.v1.endpoints.models.book_model import BookModel
from app.core.exception import NotFoundException
from app.db.session import get_db, db_dependency
from app.api.v1.endpoints.utils import safe_commit
from app.api.v1.endpoints.metrics import NOT_FOUND_BOOK_SEARCH

from app.api.v1.endpoints.metrics import BOOKS_WITH_NO_AUTHOR

router = APIRouter(
    prefix="/api/v1",
    tags=["Book"]
)


@router.get("/library/books",status_code=status.HTTP_200_OK)
async def get_all_books (db : db_dependency):
    library_books = db.query(Book).all()
    # for each book in the library
    # 1- get the author_id
    # 2- search for author information by id in the author table
    # 3- associate author information to response
    for library_book in library_books:
        author_id = library_book.author_id
        author_info = db.query(Author).filter(Author.id == author_id).first()
        if author_info is not None:
            library_book.author = {'name' : author_info.name, 'published_books' : author_info.number_of_published_books}
        else:
            BOOKS_WITH_NO_AUTHOR.inc()
    return library_books

@router.post("/library/add-book",status_code=status.HTTP_201_CREATED)
async def add_book_to_bookstore(db : db_dependency, book_info : BookModel):
    book_model = Book(**book_info.model_dump())
    db.add(book_model)
    safe_commit(db)

@router.put ("/library/update-book",status_code=status.HTTP_204_NO_CONTENT)
async def update_library_book (db : db_dependency , book_updated_info : BookModel):
    library_book = db.query(Book).filter(Book.isbn_13 == book_updated_info.isbn_13).first()
    if library_book is None:
        NOT_FOUND_BOOK_SEARCH.inc()
        raise NotFoundException('Book')


    if book_updated_info.title != "": library_book.title = book_updated_info.title
    if book_updated_info.subtitle != "": library_book.subtitle = book_updated_info.subtitle
    if book_updated_info.isbn_10 != "": library_book.isbn_10 = book_updated_info.isbn_10
    if book_updated_info.language != "": library_book.language = book_updated_info.language
    if book_updated_info.edition != "": library_book.edition = book_updated_info.edition
    if book_updated_info.publication_date != "": library_book.publication_date = book_updated_info.publication_date

    safe_commit(db)
    db.refresh(library_book)


@router.delete("/library/book/remove",status_code=status.HTTP_204_NO_CONTENT)
async def remove_book_from_library (db : db_dependency, book_isbn_13_to_remove : int = Query(gt=0)):
    library_book = db.query(Book).filter(Book.isbn_13 == book_isbn_13_to_remove).first()

    if library_book is None:
        raise NotFoundException('Book')
    db.query(Book).filter(Book.id == book_isbn_13_to_remove).delete()
    safe_commit(db)





