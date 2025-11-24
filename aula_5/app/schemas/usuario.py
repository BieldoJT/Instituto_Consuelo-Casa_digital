from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

RoleType = Literal["user", "admin"]

##============USUARIO===============##
class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3, description="Nome do usuario")
    email: str = Field(..., description="Email do usuario")

class UsuarioCreate(UsuarioBase):
    senha_hash: str = Field(..., min_length=6, description="Senha do usuario")
    role: RoleType = "user"

class UsuarioResponse(UsuarioBase):
    id: int
    role: RoleType
    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    username: str
    senha: str

