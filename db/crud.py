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
    boards = get_info(dummy_data=True)
    for i in boards:
        name = i.name

        p = models.paper(title=name, url=name, category="c")
        try:
            db.add(p)
            db.commit()
        except:
            db.rollback()
            print("paper 추가 에러 발생")

        tags = i.tags
        for tag in tags:
            t = models.tag(tag=tag)
            try:
                db.add(t)
                db.commit()
            except:
                db.rollback()
                t = db.query(models.tag).filter(models.tag.tag == t.tag).first()
                print("중복 태그")

            f_p = models.fast_paper(paper_id=p.id, tag_id=t.id)
            try:
                db.add(f_p)
                db.commit()
            except:
                db.rollback()
                print("paper 추가 에러 발생")

    return None


def remove_all_data(db: Session):
    data = db.query(models.fast_paper).all()
    for i in data:
        db.delete(i)

    data = db.query(models.paper).all()
    for i in data:
        db.delete(i)

    data = db.query(models.tag).all()
    for i in data:
        db.delete(i)

    db.commit()
    return None
