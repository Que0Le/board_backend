import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from enum import Enum


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ACCESS_TOKEN_EXPIRE_SECONDS: int = ACCESS_TOKEN_EXPIRE_MINUTES * 60
    SERVER_NAME: str = "server name"
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1"

    PROJECT_NAME: str = "project name"

    """ Token with Cookies as transport """
    COOKIES_MAX_AGE = ACCESS_TOKEN_EXPIRE_SECONDS
    COOKIES_PATH = "/"
    COOKIES_DOMAIN: bool = None
    COOKIES_SECURE: bool = True
    COOKIES_HTTP_ONLY: bool = True
    COOKIES_SAME_SITE: str = "Strict"

    DB_NAME: str = "sqlite.db"
    STATIC_DATA_DIR: str = "static_data"
    

    class Config:
        case_sensitive = True
        env_file = "../p1_data/.env"


settings = Settings()


class Roles(Enum):
    ADMIN = "admin",
    MEMBER = "member"