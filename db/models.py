from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class fast_paper(Base):
    __tablename__ = "fast_paper"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    paper_id = Column(Integer, unique=True, nullable=False)
    tag_id = Column(Integer, nullable=True)


class paper(Base):
    __tablename__ = "paper"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    category = Column(Text, nullable=True)


class tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    tag = Column(Text, nullable=False)
