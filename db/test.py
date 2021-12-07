from typing import List
import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/fast-papers/")
def read_fast_papers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_fast_papers(db, skip=skip, limit=limit)
    print(data)
    return data


@app.get("/tags/")
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_tags(db, skip=skip, limit=limit)
    print(data)
    return data


@app.get("/papers/")
def read_papers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_papers(db, skip=skip, limit=limit)
    print(data)
    return data


@app.get("/refresh/")
def refresh_data(db: Session = Depends(get_db)):
    data = crud.refresh_data(db)
    print(data)
    return data


@app.get("/paper_tags/")
def paper_tags(db: Session = Depends(get_db)):
    data = crud.get_paper_tags(db)
    print(data)
    return data


@app.get("/remove_all_data/")
def remove_all_data(db: Session = Depends(get_db)):
    data = crud.remove_all_data(db)
    print(data)
    return data


uvicorn.run(app, host="0.0.0.0", port=8000)
