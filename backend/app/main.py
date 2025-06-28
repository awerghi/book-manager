from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette import status


from app.api.v1.endpoints import book, author
from app.core.config import settings
from app.core.log import logger
from app.db.session import engine


@asynccontextmanager
async def lifespan (app : FastAPI):

    logger.info("Starting application... ")

    yield

    logger.info("shutting down application ...")



app  = FastAPI(
    lifespan= lifespan,
    title= settings.PROJECT_NAME,
    description= settings.PROJECT_DESCRIPTION,
    version= settings.PROJECT_VERSION,
    environment = settings.PROJECT_ENVIRONMENT,
    prefix= settings.API_VERSION
)

app.include_router(book.router)
app.include_router(author.router)



@app.get("/",status_code=status.HTTP_200_OK)
async def root():
    logger.info("Application is accessed")
    return {"message" : "welcome to BookNest, an app to handle your library! "}





