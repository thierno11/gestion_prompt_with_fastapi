from schema.utilisateur_schema import UtilisateurRequest,UtilisateurResponse
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
import os
import jwt
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def creer_utilisateurs(request: UtilisateurRequest, db,current_user):
    # Remplacer None explicitement si id_groupe est vide
    id_groupe = request.id_groupe if request.id_groupe else None

    # Hacher le mot de passe
    hashed_password = get_password_hash(request.password)

    # Préparer les données pour insertion
    data = request.model_dump()
    data['password'] = hashed_password
    data['id_groupe'] = id_groupe

    keys = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())

    requete = f"INSERT INTO utilisateurs ({keys}) VALUES ({placeholders}) RETURNING *"
    db.execute(requete, values)
    
    utilisateur = db.fetchone()
    db.connection.commit()

    return UtilisateurResponse(**utilisateur)


def recuperer_user_par_email(email,db):
    print(email)
    requete = "SELECT * FROM utilisateurs WHERE email=%s"
    db.execute(requete,(email,))
    utilisateur = db.fetchone()
    if not utilisateur:
        return None
    return UtilisateurResponse(**utilisateur)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




def verifier_user(db, username: str, password: str):
    user = recuperer_user_par_email(username,db)
    if not user:
        return False
    
    if not verify_password(password, user.password):
        print("password hashed")
        return False
    return user





def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def decoded_token(token,db):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    if username is None:
       return None

    user = recuperer_user_par_email(username,db)
    if user is None:
        return None
    return user

