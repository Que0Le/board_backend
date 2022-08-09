from fastapi import Header, HTTPException

from app.utilities.strings import clean_filename

from .core.db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


async def check_valid_filename(filename: str) -> str:
    sanitaired_filename = clean_filename(filename=filename)
    if sanitaired_filename == "":
        # TODO: correct name and imp and error
        raise HTTPException(status_code=400, detail=f"Invalid filename: {sanitaired_filename}")

    return sanitaired_filename