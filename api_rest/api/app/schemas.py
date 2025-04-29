# schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    admin_secret: str

class UserLogin(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    jwt: str