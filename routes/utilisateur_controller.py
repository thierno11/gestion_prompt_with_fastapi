from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated

from schema.utilisateur_schema import UtilisateurRequest, UtilisateurResponse
from services.utilisateurs_services import (
    creer_utilisateurs,
    verifier_user,
    create_access_token,
    decoded_token
)
from databases.connection import get_db

routes = APIRouter(tags=["Utilisateurs"])

auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: Annotated[str, Depends(auth_scheme)],
    db=Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = decoded_token(db=db, token=token)
    if user is None:
        raise credentials_exception
    return UtilisateurResponse(**user)

@routes.post("/", response_model=UtilisateurResponse)
def create_users(
    current_user:Annotated[UtilisateurResponse,Depends(get_current_user)],
    utilisateurs: UtilisateurRequest,
    db=Depends(get_db)
    
):
    if current_user.nom_role != "ADMINISTRATEUR":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Vous n'etes pas autorise",headers={"WWW-Authenticate": "Bearer"})
    return creer_utilisateurs(utilisateurs, db)

@routes.post("/token")
def login(
    requestForm: Annotated[OAuth2PasswordRequestForm, Depends()],
    db=Depends(get_db)
):
    user = verifier_user(db, requestForm.username,requestForm.password)
    if not user or not user.password:  # Vérifie aussi le mot de passe
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
