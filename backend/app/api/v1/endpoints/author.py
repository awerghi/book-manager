import sqlite3

from fastapi import APIRouter, Path, Query
from sqlalchemy.exc import DatabaseError
from starlette import status

from app.api.v1.endpoints.models.book_model import AuthorModel
from app.db.session import db_dependency
from app.core.exception import TransactionFailed
from app.db.models import Author, Book
from app.core.log import logger
from app.api.v1.endpoints.utils import safe_commit
from app.core.exception import NotFoundException

router = APIRouter(
    prefix="/api/v1",
    tags=["Author"]
)


@router.get("/library/authors",status_code=status.HTTP_200_OK)
async def get_all_authors(db : db_dependency):
    return db.query(Author).all()


@router.get("/library/{author_id}/books",status_code=status.HTTP_200_OK)
async def get_library_books_of_author(db : db_dependency, author_id : int = Path(gt=0)):
    try:
        author_books = db.query(Book).filter(Book.author_id==author_id).all()
        return {"author_books" : author_books}
    except sqlite3.Error as se:
        logger.info("database error occurs !",se)
    except Exception as e:
        logger.info(" something occurs while geting author books",e)


@router.post("/library/author/add",status_code=status.HTTP_201_CREATED)
async def add_author_to_library (db : db_dependency, author_info : AuthorModel):
    author_model = Author(**author_info.model_dump())
    db.add(author_model)
    safe_commit(db)

@router.put("/library/author/update",status_code=status.HTTP_204_NO_CONTENT)
async def update_library_author (db : db_dependency, author_info_payload : AuthorModel):

    author_info = db.query(Author).filter(Author.id == author_info_payload.id).first()
    if author_info is None:
        raise NotFoundException('Author')

    author_info.name = author_info_payload.name
    author_info.number_of_published_books = author_info_payload.number_of_published_books

    db.add(author_info)
    safe_commit(db)

@router.delete ("/library/author/delete",status_code=status.HTTP_204_NO_CONTENT)
async def delete_author_from_library(db : db_dependency, author_id : int = Query(gt=0)):
    author_info = db.query(Author).filter(Author.id == author_id).first()
    if author_info is None:
        raise NotFoundException('Author')
    db.delete(author_info)
    safe_commit(db)


