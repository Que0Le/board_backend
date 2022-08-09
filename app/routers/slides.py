from sqlalchemy.orm import Session
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, Form, UploadFile

from ..structures import models, schemas
from ..crud import crud
from ..dependencies import get_db
from ..core.config import settings
from ..utilities import strings

router = APIRouter()


@router.get("/slides/", response_model=list[schemas.Slide], tags=["slides"])
def read_slides(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    slides = crud.get_slides(db, skip=skip, limit=limit)
    return slides


@router.get("/slides/{slide_id}", response_model=schemas.Slide)
def read_slide(slide_id: int, db: Session = Depends(get_db)):
    db_slide = crud.get_slide(db, slide_id=slide_id)
    if db_slide is None:
        raise HTTPException(status_code=404, detail="Slide not found")
    return db_slide 


# @router.post("/slides/", response_model=schemas.Slide)
# def create_slide(slide: schemas.SlideCreate, db: Session = Depends(get_db)):
#     return crud.create_slide(db=db, slide=slide)



# @router.post(path="/uploadImages")
# async def extract_data_from_images(images: List[UploadFile] = File(...)):
#     return f"Name: {images[0].filename}, now: {datetime.now()}"


@router.post("/slides/create/")
async def handle_create_slide(
    db: Session = Depends(get_db),
    file: Optional[UploadFile] = File(None, description="A file read as UploadFile"), 
    title: str = Form(), slide_type: str = Form(),
    description: Optional[str] = Form(None), content: Optional[str] = Form(None),
):
    new_filename = await strings.clean_filename(filename=file.filename)
    if file and len(await file.read())>0:
        if new_filename=="":
            raise HTTPException(
                status_code=400, 
                detail="Filename empty or invalid"
            )
        await file.seek(0)
        with open(f"../p1_data/{settings.STATIC_DATA_DIR}/{file.filename}", "wb") as f:
            f.write(await file.read())

    slide = schemas.SlideCreate(
        title=title, 
        slide_type=slide_type if slide_type else "",
        description=description if description else "", 
        content=content if content else "",
        extra=new_filename, # will be "" if no file attached.
        config="",
    )
    print(slide)
    db_slide = crud.create_slide(db=db, slide=slide)
    if not db_slide:
        raise HTTPException(
            status_code=500, 
            detail="Couldn't create slide!"
        )
    return slide