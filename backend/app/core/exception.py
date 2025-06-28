from fastapi import HTTPException
from sqlalchemy.exc import DatabaseError


class NotFoundException(HTTPException):

    def __init__(self,entity):
        super().__init__(status_code=404,detail=f"{entity} is not found in the library, please check book information !")


class TransactionFailed(HTTPException):

    def __init__(self,entity):
        super().__init__(status_code=400,detail=f"{entity} the db transaction is not finished, an error occurs!")
