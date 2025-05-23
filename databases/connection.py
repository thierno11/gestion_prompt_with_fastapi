
from dotenv import load_dotenv
import os
from psycopg2 import connect
from psycopg2.extras import RealDictCursor

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

