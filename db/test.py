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


@app.get("/paper/")
def read_db(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_fast_papers(db, skip=skip, limit=limit)
    print(data)
    return data


uvicorn.run(app, host="0.0.0.0", port=8000)
