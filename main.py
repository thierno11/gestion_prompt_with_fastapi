from fastapi import FastAPI
from databases.connection import Base, engine
from models.utilisateurs import Utilisateur
from models.groupe import Groupe
from models.prompt import Prompt
from models.achat import Achat
from models.noter import Notes
from models.voter import Voter

# Créer les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/hello")
def hello_world():
    return {"message": "Hello WORLD"}  # ✅ Recommandé : retourner un dict/JSON, pas une string brute


