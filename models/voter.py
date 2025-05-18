from databases.connection import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKeyConstraint,PrimaryKeyConstraint,Integer,TIMESTAMP


class Voter(Base):
    __tablename__= "voter"

    id_prompt : Mapped[int] = mapped_column(Integer,nullable=False)
    id_utilisateur :Mapped[int] = mapped_column(Integer,nullable=False)
    vote :Mapped[int] = mapped_column(Integer,nullable=False)
    date_creation = mapped_column(TIMESTAMP(timezone=True),nullable=False)
    
    utilisateur :Mapped["Utilisateur"]= relationship(back_populates="votes")
    #Relation entre prompt et vote
    prompt : Mapped["Prompt"] = relationship(back_populates="votes")

    __table_args__ = (
        PrimaryKeyConstraint("id_prompt","id_utilisateur",name="pk_voter"),
        ForeignKeyConstraint(["id_prompt"], ["prompts.id_prompt"],name="fk_prompt_voter", ondelete="CASCADE"),
        ForeignKeyConstraint(["id_utilisateur"], ["Utilisateurs.id_utilisateur"],name="fk_utilisateur_voter" ,ondelete="CASCADE"),
    )