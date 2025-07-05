from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class LanguageModel (str,Enum):

    EN = "en"
    AR = "ar"
    FR = "fr"



class BookModel(BaseModel):

    title : Optional[str] = ""
    subtitle : Optional[str] = ""
    isbn_10 :  Optional[str] = ""
    isbn_13 : Optional[str] = ""
    language : LanguageModel
    edition : Optional[str] = ""
    publication_date : Optional[str] = ""
    author_id : Optional[int] = 0


class AuthorModel (BaseModel):

    id : int = Field(gt=0)
    name : str
    number_of_published_books : int
