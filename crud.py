from sqlalchemy.orm import Session
import models, schemas

def get_movies(db: Session, skip: int = 0, limit: int = 100, genre: str = None):
    query = db.query(models.Movie)
    if genre:
        query = query.filter(models.Movie.genre == genre)
    return query.offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, data: schemas.MovieCreate):
    db_movie = get_movie(db, movie_id)
    db_movie.title = data.title
    db_movie.director = data.director
    db_movie.year = data.year
    db_movie.genre = data.genre
    db_movie.rating = data.rating
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = get_movie(db, movie_id)
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie

def get_directors(db: Session):
    return db.query(models.Director).all()

def create_director(db: Session, director: schemas.DirectorCreate):
    db_director = models.Director(**director.model_dump())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director

def get_director_movies(db: Session, director_id: int):
    return db.query(models.Movie).filter(models.Movie.director_id == director_id).all()