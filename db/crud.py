from sqlalchemy.orm import Session

import models


def get_fast_papers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.fast_paper).offset(skip).limit(limit).all()



