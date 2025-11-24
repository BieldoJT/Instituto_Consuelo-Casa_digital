from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from app.database import Base


#usuario

class Usuario(Base):
    """Modelo do Usuario"""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100),nullable=False, unique=True)
    senha_hash= Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default="user")

