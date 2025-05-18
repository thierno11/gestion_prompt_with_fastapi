from databases.connection import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import Mapped,mapped_column,relationship
# from .utilisateurs import Utilisateur
from typing import List

class Groupe(Base):
    __tablename__="groupes"

    id_groupe = mapped_column(Integer,primary_key=True,autoincrement=True) 
    nom_groupe : Mapped[str] = mapped_column(String(100),unique=True,index=True,nullable=False)

    utilisateurs : Mapped[List["Utilisateur"]] = relationship(back_populates="groupe")
