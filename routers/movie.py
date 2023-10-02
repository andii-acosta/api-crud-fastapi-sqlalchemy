from fastapi import APIRouter
from fastapi import Body,Path,Query,Depends
from fastapi.responses import JSONResponse
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from fastapi.encoders import jsonable_encoder
from services.movies import MoviesServices
from schemas.movie import Movie

movie_router =  APIRouter()


@movie_router.get('/movies',tags=['movies'],response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MoviesServices(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get("/movies/{id}",tags=['movies'],response_model=Movie, status_code=200)
def get_by_id(id : int = Path(ge=1)) -> Movie:
    
    db = Session()
    result = MoviesServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie not found."})
    
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get("/movies/",tags=['movies'],response_model=List[Movie], status_code=200)
def get_by_category(category : str = Query(min_length=3, max_length=25)) -> List[Movie]:
    db = Session()
    result = MoviesServices(db).get_category(category)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie not found."})
    
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.post('/movies',tags=['movies'],response_model=dict, status_code=201)
def create(movie : Movie) -> dict:
    db = Session()
    MoviesServices(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"message":"create success."})
    

@movie_router.put('/movies/{id}',tags=["movies"],response_model=dict, status_code=201)
def update(id : int, movie : Movie) -> dict:
    db = Session()
    result = MoviesServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie not found."})
    
    MoviesServices(db).update_movie(id,movie)
    return JSONResponse(status_code=404,content={"message":"Movie update success."})


@movie_router.delete('/movies/{id}',tags=["movies"],response_model=dict, status_code=201)
def delete(id : int = Path(ge=1)) -> dict:
    
    db = Session()
    result = MoviesServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie not found."})
    
    MoviesServices(db).delete_movie(id)
    return JSONResponse(status_code=200,content={"message":"Movie delete success."})
    