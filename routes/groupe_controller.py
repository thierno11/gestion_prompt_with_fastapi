from fastapi import APIRouter,Depends,HTTPException,status
from schema.groupe_schema import GroupeResponse,GroupeSchema
from typing import List
from services.groupes_service import creer_groupe,modifier_groupe,recuperer_groupes,recuperer_groupe_par_id
from databases.connection import get_db
from utilisateur_controller import get_current_user
from typing import Annotated
from schema.utilisateur_schema import UtilisateurResponse

routes = APIRouter(prefix="/groupes",tags=["groupes"]) 

@routes.post("/",response_model=GroupeResponse)
def create_groupe(request:GroupeSchema,current_user:Annotated[UtilisateurResponse,Depends(get_current_user)],db=Depends(get_db)):
    if current_user.nom_role != "ADMINISTRATEUR":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Vous n'etes pas autorise",headers={"WWW-Authenticate": "Bearer"})
    return creer_groupe(current_user,request,db)



@routes.put("/{id}",response_model=GroupeResponse)
def update_groupe(id:int,request:GroupeSchema,current_user:Annotated[UtilisateurResponse,Depends(get_current_user)],db=Depends(get_db)):
    if current_user.nom_arole != "ADMINISTRATEUR":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Vous n'etes pas autorise",headers={"WWW-Authenticate": "Bearer"})
    return modifier_groupe(current_user,id,request,db)



@routes.get("/",response_model=List[GroupeResponse])
def get_groupes(current_user:Annotated[UtilisateurResponse,Depends(get_current_user)],db=Depends(get_db)):
    if current_user.nom_role != "ADMINISTRATEUR":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Vous n'etes pas autorise",headers={"WWW-Authenticate": "Bearer"})
    return recuperer_groupes(current_user,db)


@routes.get("/{id}",response_model=GroupeResponse)
def get_groupe(id:int,current_user:Annotated[UtilisateurResponse,Depends(get_current_user)],db=Depends(get_db)):
    if current_user.nom_role != "ADMINISTRATEUR":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Vous n'etes pas autorise",headers={"WWW-Authenticate": "Bearer"})
    return recuperer_groupe_par_id(current_user,id,db)



