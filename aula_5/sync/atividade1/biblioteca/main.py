from fastapi import FastAPI
from typing import List
from biblioteca.database import engine, Base
from biblioteca.routes import livros


Base.metadata.create_all(bind=engine)


router = FastAPI(
	title="API de Livros",
	description="API RESTful de geranciamento de livros",
	version="1.0.0"
)

#Aqui é pra incluir os routers
router.include_router(livros.router)


#router.include_router

@router.get("/")
def read_root():
	return {"mensagem": "A api ta funffando!"}
