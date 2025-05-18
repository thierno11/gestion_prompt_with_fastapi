from databases.connection import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import String,ForeignKey,Integer,text,TIMESTAMP,Text,DECIMAL,Enum,func
from datetime import timezone 
from typing import List


class Prompt(Base):
    __tablename__ = "prompts"

    id_prompt = mapped_column(Integer,primary_key=True,autoincrement=True)

    titre:Mapped[str] = mapped_column(String(100))
    libelle : Mapped[str] = mapped_column(Text,nullable=False)
    prix : Mapped[float] = mapped_column(DECIMAL(10,2),default=1000,server_default=text("1000"))
    status: Mapped[str] =mapped_column(Enum("EN ATTENTE","A SUPPRIMER","ACTIVE","A REVOIR","RAPPEL",name="statut"),nullable=False,default="EN ATTENTE",server_default="EN ATTENTE")
    date_creation = mapped_column(TIMESTAMP(timezone=True),nullable=False,default= timezone.utc,server_default=func.now())
    date_modification = mapped_column(TIMESTAMP(timezone=True),nullable=False,default=timezone.utc,server_default=func.now())
    id_utilisateur : Mapped[int] = mapped_column(ForeignKey("Utilisateurs.id_utilisateur",name="fk_utilisateurs_prompts",ondelete="CASCADE"),nullable=False)

    # RELATION ENTRE PROMPTS ET UTILISATEURS
    utilisateur : Mapped["Utilisateur"] = relationship(back_populates="prompts")
    #Relation entre Achat et prompts
    achats :Mapped[List["Achat"]] = relationship(back_populates="prompts")

    #relation entre prompt et votes 
    votes : Mapped[List["Voter"]]=relationship(back_populates="prompt")
    #Relation entre [rompte et note ]
    notes : Mapped[List["Noter"]]=relationship(back_populates="prompt")