
from dotenv import load_dotenv
import os
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from .sript import table_utilisateur,table_groupes,ENUM_ROLE,ENUM_STATUS

load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "projet_fastapi")

conn=connect(database = DB_NAME, 
            user = DB_USER, 
            host= DB_HOST,
            password = DB_PASSWORD,
            port = DB_PORT,cursor_factory=RealDictCursor)


def get_db():
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

def get_connection():
    """Gestionnaire de contexte pour obtenir une connexion à la base de données."""
    try:
        conn=connect(database = DB_NAME, 
            user = DB_USER, 
            host= DB_HOST,
            password = DB_PASSWORD,
            port = DB_PORT,cursor_factory=RealDictCursor)
        return conn
    finally:
        print("terminee")


def init_database():
    """Initialise la structure de la base de données."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                # Exécution des scripts dans une transaction
                cursor.execute(ENUM_ROLE)
                cursor.execute(ENUM_STATUS)
                cursor.execute(table_groupes)
                cursor.execute(table_utilisateur)
                # Validation explicite des modifications
                conn.commit()
                print("Base de données initialisée avec succès.")
            except Exception as e:
                conn.rollback()
                print(f"Erreur lors de l'initialisation de la base de données: {e}")
                raise

