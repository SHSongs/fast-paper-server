from sqlalchemy.orm import Session

import models
from domain.crawler import get_info, Board


def get_fast_papers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.fast_paper).offset(skip).limit(limit).all()


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.tag).offset(skip).limit(limit).all()


def get_papers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.paper).offset(skip).limit(limit).all()


def get_paper_tags(db: Session):
    t = db.query(models.fast_paper.paper_id, models.tag.tag, models.paper.title). \
        join(models.tag, models.fast_paper.tag_id == models.tag.id). \
        join(models.paper, models.fast_paper.paper_id == models.paper.id).all()
    return t


def refresh_data(db: Session):
    boards = get_info()
    for i in boards:
        tags = i.tags
        for tag in tags:

            t = models.tag(tag=tag)
            try:
                db.add(t)
                db.commit()
            except:
                print("중복 태그")
    return None