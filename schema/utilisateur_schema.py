from pydantic import BaseModel,EmailStr
from typing import Optional
from enum import Enum

class NomRoleEnum(str, Enum):
    UTILISATEUR = "UTILISATEUR"
    ADMINISTRATEUR = "ADMINISTRATEUR"


class UtilisateurSchema(BaseModel):
    nom:str
    prenom:str
    email: EmailStr
    nom_role:NomRoleEnum
    id_groupe:Optional[int] = None

class UtilisateurRequest(UtilisateurSchema):
    password:str

class UtilisateurResponse(UtilisateurSchema):
    id_utilisateur : int

class UpdateUtilisateur(BaseModel):
    nom:Optional[str]
    prenom:Optional[str]
    email: Optional[EmailStr]
    nom_role:Optional[NomRoleEnum]
    id_groupe:Optional[int] 
    password:Optional[str]