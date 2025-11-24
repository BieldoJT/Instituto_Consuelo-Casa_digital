from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


RoleType = Literal["user", "admin"]

##============PRODUTO===============##

class ProdutoBase(BaseModel):
    """Schema base para produto (dados comuns)"""
    nome: str = Field(..., min_length=3, max_length=100, description="Nome do produto")
    descricao: Optional[str] = Field(None, max_length=500, description="Descrição detalhada")
    preco: float = Field(..., gt=0, description="Preço deve ser maior que zero")
    estoque: int = Field(default=0, ge=0, description="Quantidade em estoque")
    categoria: str = Field(..., min_length=3, description="Categoria do produto")

class ProdutoCreate(ProdutoBase):
    """Schema para criação de produto (dados de entrada)"""
    pass

class ProdutoUpdate(BaseModel):
    """Schema para atualização (todos os campos opcionais)"""
    nome: Optional[str] = Field(None, min_length=3, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: Optional[float] = Field(None, gt=0)
    estoque: Optional[int] = Field(None, ge=0)
    categoria: Optional[str] = Field(None, min_length=3)

class ProdutoEstoqueUpdate(BaseModel):
    estoque: int = Field(...,gt=0, description="Novo estoque do produto")

class ProdutoResponse(ProdutoBase):
    """Schema para resposta (inclui campos do banco)"""
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True  # Permite conversão de modelos SQLAlchemy

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


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"



