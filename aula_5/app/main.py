from fastapi import FastAPI, HTTPException
from typing import List
from app.database import engine, Base
from app.routes import produtos, auth


# Cria a instância da aplicação FastAPI
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Produtos",
    description="API RESTful para gerenciar produtos de uma loja",
    version="1.0.0"
)

# Incluir routers (modular!)
app.include_router(produtos.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"mensagem": "API de Produtos está funcionando!"}
