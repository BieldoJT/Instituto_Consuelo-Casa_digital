from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Produto(Base):
    """Modelo de produto para o banco de dados"""

    __tablename__ = "produtos"  # Nome da tabela no PostgreSQL

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False, index=True)
    descricao = Column(String(500), nullable=True)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0, nullable=False)
    categoria = Column(String(50), nullable=False, index=True)

    # Timestamps automáticos
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', preco={self.preco})>"

class Usuario(Base):
    """Modelo do Usuario"""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100),nullable=False, unique=True)
    senha_hash= Column(String(255), nullable=False)

