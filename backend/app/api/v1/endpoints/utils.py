from fastapi import HTTPException
from sqlalchemy.exc  import IntegrityError, SQLAlchemyError
from starlette import status

from app.api.v1.endpoints.metrics import BOOKS_CREATED


def safe_commit(db):
    try:
        db.commit()
        BOOKS_CREATED.inc()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity error: constraint violation or invalid foreign key."
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )