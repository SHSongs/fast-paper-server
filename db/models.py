from sqlalchemy import Column, ForeignKey, Integer, Text

from database import Base


class fast_paper(Base):
    __tablename__ = "fast_paper"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    paper_id = Column(Integer, ForeignKey("paper.id"))
    tag_id = Column(Integer, ForeignKey("tag.id"))


class paper(Base):
    __tablename__ = "paper"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    category = Column(Text, nullable=True)


class tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    tag = Column(Text, nullable=False, unique=True)
