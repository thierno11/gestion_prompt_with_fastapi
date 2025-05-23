from schema.groupe_schema import GroupeResponse,GroupeSchema
from schema.utilisateur_schema import UtilisateurResponse

def creer_groupe(request: GroupeSchema, db):
    data = request.model_dump()
    keys = ", ".join(data.keys())                     
    placeholders = ", ".join(["%s"] * len(data))      
    values = tuple(data.values())                     

    requete = f"INSERT INTO GROUPES({keys}) VALUES ({placeholders}) RETURNING *"
    db.execute(requete, values)
    groupe = db.fetchone()
    db.connection.commit()

    return GroupeResponse(**groupe)


def modifier_groupe(id: int, request: GroupeSchema, db):
    # 1) Récupérer l'enregistrement existant
    select_sql = "SELECT * FROM GROUPES WHERE id_groupe = %s"
    db.execute(select_sql, (id,))
    groupe = db.fetchone()
    if not groupe:
        return None  # ou lever une exception, selon ton design

    # 2) Préparer les données à mettre à jour
    data = request.model_dump()              
    columns = list(data.keys())              
    values = list(data.values())            

    # 3) Construire la clause SET dynamiquement
    #    ex: "nom_groupe = %s, description = %s"
    set_clause = ", ".join(f"{col} = %s" for col in columns)

    # 4) Construire et exécuter le UPDATE
    update_sql = f"""
        UPDATE GROUPES
           SET {set_clause}
         WHERE id_groupe = %s
         RETURNING *
    """
    # on ajoute l'id en dernier argument
    db.execute(update_sql, (*values, id))

    # 5) Récupérer la ligne mise à jour
    updated = db.fetchone()
    db.connection.commit()

    # 6) Retourner une réponse Pydantic
    return GroupeResponse(**updated)


def recuperer_groupes(db):
    db.execute("SELECT * FROM groupes")
    groupes = db.fetchall()
    groupes = map(lambda g : GroupeResponse(**g),groupes)
    return groupes

def recuperer_groupe_par_id(id:int,db):
    db.execute("SELECT * FROM groupes where id_groupe=%s",(id,))
    groupe = db.fetchone()
    groupe = GroupeResponse(**groupe)
    return groupe