from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from biblioteca.models import Livro
from biblioteca.schemas import LivroCreate, LivroResponse, LivroUpdate

#criar o router pro livro
router = APIRouter(
	prefix="/livros", # Tod
	tags=["Livros"] #pro Swagger
)

## CREATE

@router.post("/", response_model=LivroResponse, status_code=status.HTTP_201_CREATED)
def criar_livro(livro: LivroCreate, db:Session = Depends(get_db)):
	"Cria um novo livro no banco"
	#criando instancia de livro pelo sqlalchemy
	db_livro = Livro(
		titulo=livro.titulo,
		autor=livro.autor,
		ano_publicacao=livro.ano_publicacao,
		isbn=livro.isbn,
		disponivel=livro.disponivel
	)
	db.add(db_livro)
	db.commit()
	db.refresh(db_livro)

	return db_livro


# READ DE GERAL
@router.get("/", response_model=List[LivroResponse])
def listar_livros(
	skip: int = 0,
	limit: int = 100,
	autor: str = None,
	disponivel: bool = None,
	db: Session = Depends(get_db)
):
	"""Lista de livros com pgaginação e filtro"""

	#inicia a query - SELECT * FROM livros
	query = db.query(Livro)

	if autor and disponivel:
		query = query.filter(
			Livro.autor == autor,
			Livro.disponivel == disponivel)
	elif(autor):
		query = query.filter(Livro.autor == autor)
	elif(disponivel):
		query = query.filter(Livro.disponivel == disponivel)

	livro = query.offset(skip).limit(limit).all()

	return livro


#READ ESPECIFICO
@router.get("/{livro_id}", response_model=LivroResponse)
def obter_Livro(livro_id: int, db: Session = Depends(get_db)):
	"Busca um livro especifico por ID"

	livro = db.query(Livro).filter(Livro.id == livro_id).first()

	if not livro:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Livro com ID {livro_id} não encontrado"
		)
	return livro


##UPDATE DE UM LIVRO
@router.put("/{livro_id}", response_model=LivroResponse)
def atualizar_livro(
	livro_id: int,
	livro_update: LivroUpdate,
	db:Session = Depends(get_db)
):
	"""Atualiza um livro existente (podendo ser uma atualização parcial)
	retorna o os campos q atualizou
	"""

	livro = db.query(Livro).filter(Livro.id == livro_id).first()

	if not livro:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Livro com ID {livro_id} não encontrado"
		)

	#pega apenas os cmapos que foram alterados
	##model_dump(exclude_unset=True)
	update_data = livro_update.model_dump(exclude_unset=True)

	#atualiza cada campo
	for campo, valor in update_data.items():
		setattr(livro, campo, valor)

	#sempre que mexe no campo, fazer commit
	db.commit()
	db.refresh(livro)

	return livro


##delete
@router.delete("/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_livro(livro_id: int, db:Session = Depends(get_db)):
	"""Remove um produto do banco

	204 = sucesso sem corpo na resposta"""

	db_livro = db.query(Livro).filter(Livro.id == livro_id).first()

	if not db_livro:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Livro com ID {livro_id} não encontrado"
		)

	db.delete(db_livro)
	db.commit()

	return None ##retorna 204




