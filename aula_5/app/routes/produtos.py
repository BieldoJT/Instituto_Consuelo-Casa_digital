from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Produto
from app.schemas import ProdutoCreate, ProdutoResponse, ProdutoUpdate

# Cria o router para organizar as rotas
router = APIRouter(
    prefix="/produtos",  # Todas as rotas começam com /produtos
    tags=["Produtos"]    # Agrupa na documentação Swagger
)

# ==================== CREATE ====================
@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo produto no banco de dados.

    O que acontece aqui:
    1. FastAPI recebe JSON e valida com ProdutoCreate
    2. Criamos uma instância do modelo Produto
    3. Adicionamos à sessão do banco (staging)
    4. commit() salva permanentemente
    5. refresh() busca dados gerados (ID, timestamps)
    6. Retorna produto criado (FastAPI converte em JSON)
    """
    # Cria instância do modelo SQLAlchemy
    db_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        estoque=produto.estoque,
        categoria=produto.categoria
    )

    db.add(db_produto)  # Adiciona à sessão (ainda não salvou!)
    db.commit()         # AGORA salva no banco de dados
    db.refresh(db_produto)  # Busca valores gerados pelo banco (ID, timestamps)

    return db_produto

# ==================== READ (todos) ====================
@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(
    skip: int = 0,
    limit: int = 100,
    categoria: str = None,
    db: Session = Depends(get_db)
):
    """
    Lista produtos com paginação e filtro opcional.

    Paginação: evita retornar milhares de registros de uma vez
    - skip=0, limit=10 → primeiros 10
    - skip=10, limit=10 → próximos 10 (página 2)
    - skip=20, limit=10 → próximos 10 (página 3)
    """
    # Inicia a query
    query = db.query(Produto)

    # Aplica filtro se categoria foi informada
    if categoria:
        query = query.filter(Produto.categoria == categoria)

    # Aplica paginação e executa
    produtos = query.offset(skip).limit(limit).all()

    return produtos

# ==================== READ (um específico) ====================
@router.get("/{produto_id}", response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    """
    Busca um produto específico por ID.

    .first() retorna o primeiro resultado ou None
    Se None, lançamos HTTPException com 404
    """
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )

    return produto

# ==================== UPDATE ====================
@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    produto_update: ProdutoUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza um produto existente (atualização parcial permitida).

    model_dump(exclude_unset=True) retorna apenas campos que foram
    enviados na requisição, ignorando os None/não informados.
    """
    # Busca o produto
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not db_produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )

    # Pega apenas os campos que foram enviados
    update_data = produto_update.model_dump(exclude_unset=True)

    # Atualiza cada campo
    for campo, valor in update_data.items():
        setattr(db_produto, campo, valor)  # produto.campo = valor

    db.commit()
    db.refresh(db_produto)

    return db_produto

# ==================== DELETE ====================
@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    """
    Remove um produto do banco de dados.

    204 No Content = sucesso, mas sem corpo na resposta
    """
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not db_produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado"
        )

    db.delete(db_produto)
    db.commit()

    return None  # 204 não retorna conteúdo
