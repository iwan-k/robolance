from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class RobolancerDB(Base):
    __tablename__ = "robolancer"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(30), index=True)
    description: Mapped[Optional[str]]
    thumbnail: Mapped[str] = mapped_column(String(120))
    location: Mapped[Optional[str]]
    hourly_rate: Mapped[int]


# class RobolancerDB(Base):
#     __tablename__ = "robolancer"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String)
#     thumbnail = Column(String)
#     location = Column(String)
#     hourly_rate = Column(Integer)



class BlogPostBaseDB(Base):
    __tablename__ = "blogpost"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image = Column(String)
    text = Column(String)