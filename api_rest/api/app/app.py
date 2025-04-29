# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import os

from app.models import Base, User
from app.database import get_db, engine
from app.schemas import UserCreate, UserLogin, Token
from app.auth import (
    hash_password,
    create_jwt_token,
    get_user_by_email,
    verify_password,
    decode_jwt
)
from app.scraping import get_bovespa_data


Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBearer()

# Endpoint de registro de usuários
@app.post("/registrar", response_model=Token)
def registrar(user_data: UserCreate, db: Session = Depends(get_db)):

    # Faz a autenticação para registro dos usuarios - autenticaçãoa adm
    if user_data.admin_secret != os.getenv("ADMIN_SECRET", "superadminsegredo"):
        raise HTTPException(status_code=401, detail="Acesso não autorizado. Secret inválido.")
    
    if get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=409, detail="Email já registrado")

    hashed_password = hash_password(user_data.senha)
    novo_usuario = User(
        nome=user_data.nome,
        email=user_data.email,
        senha_hash=hashed_password
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    jwt = create_jwt_token(novo_usuario)
    return {"jwt": jwt}

# Endpoint de login de usuários
@app.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email não encontrado")

    if not verify_password(user_data.senha, user.senha_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha incorreta")

    jwt = create_jwt_token(user)
    return {"jwt": jwt}

# Endpoint de consulta de dados com autenticação via JWT
@app.get("/consultar")
def consultar(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_data = decode_jwt(token)
    if not user_data:
        raise HTTPException(status_code=403, detail="Token inválido ou expirado")

    dados = get_bovespa_data()
    return {"dados": dados}
