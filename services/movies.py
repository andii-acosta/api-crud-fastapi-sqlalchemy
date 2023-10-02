from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MoviesServices():
    
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self,id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_category(self,category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self,Movie):
        new_movie = MovieModel(**Movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self,id,data : Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.year = data.year
        movie.overview = data.overview
        movie.category = data.category
        movie.rating = data.rating
        self.db.commit()
        return
    
    def delete_movie(self,id : int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return
        
    