from sqlalchemy import String,Integer,Enum,ForeignKey
from sqlalchemy.orm import mapped_column,Mapped,relationship
from databases.connection import Base
from typing import List
class Utilisateur(Base):
    __tablename__="Utilisateurs"

    id_utilisateur = mapped_column(Integer,primary_key=True,autoincrement=True)
    nom : Mapped[str] = mapped_column(String(50))
    prenom : Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    password : Mapped[str] = mapped_column(String,nullable=False)
    nom_role : Mapped[str] = mapped_column(Enum("ADMINISTRATEUR","UTILISATEUR",name="role"),nullable=False,default="UTILISATEUR")
    id_groupe = mapped_column(ForeignKey("groupes.id_groupe",ondelete="SET NULL"))
    #Relation entre groupes et utilisateurs
    groupe : Mapped["Groupe"] = relationship(back_populates="utilisateurs")
    #Relation entre prompts et utilisateurs
    prompts : Mapped[List["Prompt"]] = relationship(back_populates="utilisateur")
    #relation entre Utilisateurs et votes 
    votes : Mapped[List["Voter"]]=relationship(back_populates="utilisateur")
    #Relation entre utilisateur et note ]
    notes : Mapped[List["Noter"]]=relationship(back_populates="utilisateur")