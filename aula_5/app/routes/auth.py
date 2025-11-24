from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from passlib.hash import pbkdf2_sha256
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from app.utils import config
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.schemas.token import Token




router = APIRouter(
	prefix="/auth",
	tags=["Auth"]
)

def get_password_hash(password: str) -> str:
    return pbkdf2_sha256.hash(password)

@router.post("/registro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def cria_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
	"""
	Cria um novo usuario
	"""

	ja_existe = db.query(Usuario).filter(
		Usuario.username == usuario.username or Usuario.email == usuario.email
		).first()

	if ja_existe:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Usuario ja cadastrado!"
		)
	db_usuario = Usuario(
		username = usuario.username,
		email = usuario.email,
		senha_hash = get_password_hash(usuario.senha_hash),
		role = usuario.role
	)

	db.add(db_usuario)
	db.commit()
	db.refresh(db_usuario)

	return db_usuario

@router.post("/login", response_model=Token)
def login_usuario(
	form_data: OAuth2PasswordRequestForm = Depends(),
	db: Session = Depends(get_db)
	):
	# form_data.username e form_data.password vêm do Swagger
	usuario = config.authenticate_user(db, form_data.username, form_data.password)

	if not usuario:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail= "Usuario ou senha invalidos",
			headers={"WWW-Authenticate": "Bearer"}
		)

	access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

	access_token = config.create_access_token(
		data={"sub": str(usuario.id)},
		expires_delta=access_token_expires
		)

	return Token(access_token=access_token, token_type="bearer")

