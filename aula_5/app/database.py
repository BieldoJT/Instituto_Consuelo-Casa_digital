from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão do PostgreSQL
# Formato: postgresql://usuario:senha@host:porta/nome_banco
DATABASE_URL = "postgresql://gabriel:Dragonoide01@localhost:5432/loja_db"

# Engine: gerencia a conexão com o banco
engine = create_engine(
    DATABASE_URL,
    echo=True  # Mostra SQL no console (útil para debug)
)

# SessionLocal: factory para criar sessões de banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base: classe base para os modelos
Base = declarative_base()

# Dependency para obter sessão do banco
def get_db():
    """
    Cria uma sessão de banco de dados e garante que será fechada.
    Uso: como dependência do FastAPI
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
