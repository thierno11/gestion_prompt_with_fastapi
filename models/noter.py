from databases.connection import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKeyConstraint,PrimaryKeyConstraint,Integer,TIMESTAMP,DECIMAL


class Notes(Base):
    __tablename__= "noter"

    id_prompt : Mapped[int] = mapped_column(Integer,nullable=False)
    id_utilisateur :Mapped[int] = mapped_column(Integer,nullable=False)
    note :Mapped[int] = mapped_column(DECIMAL(10,2),nullable=False)
    date_creation = mapped_column(TIMESTAMP(timezone=True),nullable=False)
    
    utilisateur :Mapped["Utilisateur"]= relationship(back_populates="notes")
    #Relation entre prompt et note
    prompt : Mapped["Prompt"] = relationship(back_populates="notes")

    __table_args__ = (
        PrimaryKeyConstraint("id_prompt","id_utilisateur",name="pk_noter"),
        ForeignKeyConstraint(["id_prompt"], ["prompts.id_prompt"],name="fk_prompt_noter", ondelete="CASCADE"),
        ForeignKeyConstraint(["id_utilisateur"], ["Utilisateurs.id_utilisateur"],name="fk_utilisateur_noter" ,ondelete="CASCADE"),
    )