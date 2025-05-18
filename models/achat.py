from databases.connection import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,ForeignKey


class Achat(Base):
    __tablename__ = "Achtas"

    id_achat = mapped_column(Integer,autoincrement=True,primary_key=True)
    nom_acheteur : Mapped[str] = mapped_column(String(50))
    prenom_acheteur :Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(100))
    montant : Mapped[float] = mapped_column(DECIMAL(10,2),nullable=False)
    id_prompt : Mapped[int] = mapped_column(Integer,ForeignKey("prompts.id_prompt",name="fk_prompts_achat"),nullable=False)

    #Releation entre prompt et Achat 
    prompt :Mapped["Prompt"] = relationship(back_populates="achats")
