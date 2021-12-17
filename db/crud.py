from sqlalchemy.orm import Session
from typing import List
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
    boards: List[Board] = get_info(dummy_data=True)

    def addDB(data, except_func=None, *except_args):
        try:
            db.add(data)
            db.commit()
        except:
            db.rollback()
            data = except_func(except_args)

        return data

    for board in boards:
        name = board.name
        p = models.paper(title=name.split('/')[-1], url=name, category=board.category)
        addDB(p)

        for tag in board.tags:
            t = models.tag(tag=tag)
            t = addDB(t, lambda args: db.query(models.tag).filter(models.tag.tag == args[0]).first(), t.tag)

            f_p = models.fast_paper(paper_id=p.id, tag_id=t.id)
            addDB(f_p)

    return None


def remove_all_data(db: Session):
    def deleteTable(table):
        data = db.query(table).all()
        for i in data:
            db.delete(i)
        db.commit()

    deleteTable(models.fast_paper)
    deleteTable(models.paper)
    deleteTable(models.tag)
    return None
