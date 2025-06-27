from pydantic_settings import BaseSettings


class Settings(BaseSettings):


    # Project configuration

    PROJECT_NAME : str = "BookNest"
    PROJECT_VERSION : str = "1.0"
    PROJECT_DESCRIPTION : str = "Handle an online library, add, delete and update book information"
    PROJECT_ENVIRONMENT : str = "DEV"
    API_VERSION: str = "/api/v1"
    LOG_LEVEL : str = "INFO"



settings = Settings()
