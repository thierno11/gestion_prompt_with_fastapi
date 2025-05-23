from pydantic import BaseModel


class GroupeSchema(BaseModel):
    nom_groupe:str

class GroupeResponse(GroupeSchema):
    id_groupe:int