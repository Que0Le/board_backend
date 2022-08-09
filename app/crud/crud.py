from sqlalchemy.orm import Session

from ..structures import models, schemas


""" nnn   """
def get_slide(db: Session, slide_id: int):
    return db.query(models.Slide).filter(models.Slide.id == slide_id).first()


def create_slide(db: Session, slide: schemas.SlideCreate):
    db_slide = models.Slide(
        title=slide.title,
        slide_type=slide.slide_type,
        description=slide.description,
        content=slide.content,
        extra=slide.extra,
        config=slide.config
    )
    db.add(db_slide)
    db.commit()
    db.refresh(db_slide)
    return db_slide


def get_slides(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Slide).offset(skip).limit(limit).all()


"""  """
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


"""  """
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item