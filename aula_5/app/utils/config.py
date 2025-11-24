# app/core/config.py
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from typing import Optional
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from app.models.usuario import Usuario



SECRET_KEY = "cf1639d5201dd6c301c02b86cf8ff87bb255029a962b98a82e29c57fa28f2d33"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



def verify_password(plain_password: str, hashed_password: str) -> bool:
	return pbkdf2_sha256.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()

    # Agora usamos timezone-aware em UTC
    now_utc = datetime.now(timezone.utc)

    if expires_delta:
        expire = now_utc + expires_delta
    else:
        expire = now_utc + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # O python-jose aceita datetime com tzinfo=UTC
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user_by_username(db: Session, username: str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.username == username).first()

def authenticate_user(db: Session, username: str, senha: str) -> Usuario | None:
    usuario = get_user_by_username(db, username)
    if not usuario:
        return None
    if not verify_password(senha, usuario.senha_hash):
        return None
    return usuario

def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id: Optional[str] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    usuario = db.query(Usuario).filter(Usuario.id == int(user_id)).first()
    if usuario is None:
        raise credentials_exception

    return usuario



def require_auth(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """
    Dependência para garantir que o usuário está autenticado.
    Retorna o usuário logado.
    """
    return current_user

def require_roles(allowed_roles: list[str]):
    """
    Cria uma dependência que só permite usuários com certas roles.
    Uso: Depends(require_roles(["admin"]))
    """
    def dependency(current_user: Usuario = Depends(get_current_user)) -> Usuario:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem permissão para acessar este recurso."
            )
        return current_user

    return dependency

