from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title='Movie API', version='1.0')

@app.get('/movies', response_model=list[schemas.MovieResponse])
def get_movies(skip: int = 0, limit: int = 10, genre: str = None, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit, genre=genre)

@app.get('/movies/{movie_id}', response_model=schemas.MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.post('/movies', response_model=schemas.MovieResponse, status_code=201)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@app.put('/movies/{movie_id}', response_model=schemas.MovieResponse)
def update_movie(movie_id: int, data: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.update_movie(db, movie_id, data)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.delete_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {'message': 'Deleted successfully'}

@app.get('/directors', response_model=list[schemas.DirectorResponse])
def get_directors(db: Session = Depends(get_db)):
    return crud.get_directors(db)

@app.post('/directors', response_model=schemas.DirectorResponse, status_code=201)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return crud.create_director(db, director)

@app.get('/directors/{director_id}/movies', response_model=list[schemas.MovieResponse])
def get_director_movies(director_id: int, db: Session = Depends(get_db)):
    return crud.get_director_movies(db, director_id)