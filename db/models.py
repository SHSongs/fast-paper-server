from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class fast_paper(Base):
    __tablename__ = "fast_paper"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    paper_id = Column(Integer, unique=True, nullable=False)
    tag_id = Column(Integer, nullable=True)
