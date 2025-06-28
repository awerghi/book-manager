from enum import Enum

from pydantic import BaseModel, Field


class LanguageModel (str,Enum):

    EN = "en"
    AR = "ar"
    FR = "fr"



class BookModel(BaseModel):

    id : int = Field(gt=0)
    title : str
    subtitle : str
    isbn_10 :  str = Field(min_length=10,max_length=10)
    isbn_13 : str = Field(min_length=13,max_length=13)
    language : LanguageModel
    edition : str
    publication_date : str
    author_id : int


class AuthorModel (BaseModel):

    id : int = Field(gt=0)
    name : str
    number_of_published_books : int
