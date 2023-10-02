from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config.database import engine,Base
from middlewares.error_handler import Error_handler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Api demo FastAPI"
app.version = "0.0.1"

app.add_middleware(Error_handler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get("/",tags=['home'],response_model=dict, status_code=200)
def main() -> dict:
    return JSONResponse(status_code=200, content={"message": "Welcome, this is an API created for Learn FastAPI crud"})
