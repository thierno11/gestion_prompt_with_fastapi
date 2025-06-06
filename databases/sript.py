ENUM_ROLE = """
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'role') THEN
        CREATE TYPE role AS ENUM ('ADMINISTRATEUR', 'UTILISATEUR');
    END IF;
END
$$;

"""

ENUM_STATUS = """
    DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'statut') THEN
        CREATE TYPE statut AS ENUM (
            'EN ATTENTE',
            'ACTIVE',
            'RAPPEL',
            'A REVOIR',
            'A SUPPRIMER'
        );
    END IF;
END
$$;
"""

table_groupes = """
    CREATE TABLE IF NOT EXISTS GROUPES(
        id_groupe SERIAL,
        nom_groupe VARCHAR(100) UNIQUE,
        CONSTRAINT pk_groupes PRIMARY KEY(id_groupe)
    )
"""


table_utilisateur = """ 
CREATE TABLE IF NOT EXISTS UTILISATEURS(
    id_utilisateur SERIAL,
    nom VARCHAR(50),
    prenom VARCHAR(100),
    email VARCHAR(70) UNIQUE,
    password VARCHAR,
    nom_role ROLE,
    id_groupe INT,
    CONSTRAINT pk_utilisateurs PRIMARY KEY(id_utilisateur),
    CONSTRAINT fk_groupes_utilisateurs FOREIGN KEY(id_groupe) REFERENCES GROUPES(id_groupe)
)
"""

table_prompt = """
    CREATE TABLE IF NOT EXISTS  PROMPTS(
        id_prompt SERIAL,
        libelle TEXT,
        status  STATUT,
        prix DOUBLE PRECISION DEFAULT 1000,
        date_creation TIMESTAMP DEFAULT NOW(),
        date_modification TIMESTAMP DEFAULT NOW(),
        id_utilisateur INT,
        CONSTRAINT pk_prompts PRIMARY KEY(id_prompt),
        CONSTRAINT fk_utilisateurs_prompts FOREIGN KEY(id_utilisateur) REFERENCES UTILISATEURS(id_utilisateur)
    )
"""


table_notation = """
    CREATE TABLE IF NOT EXISTS NOTATION(
        id_utilisateur INT,
        id_prompt INT,
        note INT,
        date_note DATE,
        CONSTRAINT fk_utilisateurs_notation FOREIGN KEY(id_utilisateur)  REFERENCES UTILISATEURS (id_utilisateur),
        CONSTRAINT fk_prompts_notation FOREIGN KEY (id_prompt)  REFERENCES PROMPTS (id_prompt),
        CONSTRAINT pk_notation PRIMARY KEY(id_utilisateur,id_prompt)
    )

"""

table_voter = """
    CREATE TABLE IF NOT EXISTS VOTER(
        id_utilisateur INT,
        id_prompt INT,
        vote INT,
        date_vote DATE,
        CONSTRAINT fk_utilisateurs_notation_voter FOREIGN KEY (id_utilisateur)  REFERENCES UTILISATEURS (id_utilisateur),
        CONSTRAINT fk_prompts_notation_voter FOREIGN KEY (id_prompt)  REFERENCES PROMPTS (id_prompt),
        CONSTRAINT pk_voter PRIMARY KEY(id_utilisateur,id_prompt)
    )
"""

table_Achat = """
    CREATE TABLE IF NOT EXISTS ACHATS(
        id_achat SERIAL PRIMARY KEY,
        nom_acheteur VARCHAR(50),
        email_acheteur varchar(50),
        montant NUMERIC(10,2),
        id_prompt int,
        CONSTRAINT fk_prompts_achat FOREIGN KEY(id_prompt) REFERENCES PROMPTS(id_prompt))
"""