from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)
    genre = Column(String)
    rating = Column(Float)
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=True)