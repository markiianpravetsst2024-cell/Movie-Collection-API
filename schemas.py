from typing import Optional
from pydantic import BaseModel, Field

class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float = Field(ge=0.0, le=10.0)
    director_id: Optional[int] = None

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True

class DirectorBase(BaseModel):
    name: str
    country: str

class DirectorCreate(DirectorBase):
    pass

class DirectorResponse(DirectorBase):
    id: int

    class Config:
        from_attributes = True