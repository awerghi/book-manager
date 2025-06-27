from fastapi import HTTPException


class BookNotFoundException(HTTPException):

    def __init__(self):
        super().__init__(status_code=404,detail="Book is not found in the library, please check book information !")