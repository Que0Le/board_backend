from fastapi import FastAPI, File, Request, UploadFile, Depends

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.routers import slides

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users, data, slides

from app.core.config import settings
# app = FastAPI(dependencies=[Depends(get_query_token)])
from sqlalchemy.orm import Session

from .structures import models
from .core.db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="./static")


# app.mount("/static", StaticFiles(directory="./data/static"), name="static")
# app.mount("/static-data", StaticFiles(directory="../static_data"), name="static_data")

# TODO: check if static data folder exist

# TODO: check user and data eixst


@app.get("/upload", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("upload_page.html", {"request": request})


app.include_router(users.router)
app.include_router(items.router)
app.include_router(slides.router)
app.include_router(data.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}