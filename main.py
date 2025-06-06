
from fastapi.middleware.cors import CORSMiddleware
from routes.groupe_controller import routes
from routes import utilisateur_controller
from fastapi import FastAPI,Depends
from databases.connection import init_database

init_database()

app = FastAPI()


app.include_router(routes)
app.include_router(utilisateur_controller.routes)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])