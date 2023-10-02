from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id : Optional[int] | None=None
    year : int
    category : str = Field(max_length=25)
    title : str = Field(max_length=50)
    overview : str = Field(max_length=50)
    rating: float
    
    class Config:
        shema_extra = {
            "example": {
                "id": 1,
                "year":"2014",
                "title":"interestelar",
                "category":"Ciencia ficción",
                "overview":"Descripcion",
                "rating":"5"
            }
        }