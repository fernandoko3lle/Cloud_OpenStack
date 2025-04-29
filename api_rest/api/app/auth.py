# auth.py
import bcrypt
import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import User
import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersegredo")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def create_jwt_token(user: User) -> str:
    payload = {
        "sub": str(user.id),
        "name": user.nome,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

