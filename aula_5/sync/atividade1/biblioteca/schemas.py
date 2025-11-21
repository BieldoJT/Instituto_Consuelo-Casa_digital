from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

#Schema do livro

class LivroBase(BaseModel):
	"""schema base para livro"""
	titulo:str = Field(..., max_length=200, description="Titulo do livro")
	autor:str = Field(..., min_length=3, description="Autor do livro")
	ano_publicacao:int = Field(..., gt=0, description="Ano de publicação do livro")
	isbn:str = Field(...,unique=True, min_length=13, max_length=50)
	disponivel:bool = Field(default=True, description="Booleano pra definir se livro esta disponivel")

#criar isso para poder criar o livro
class LivroCreate(LivroBase):
	"""schema para criação do livro"""
	pass

#classe para poder fazer PUT na api, sem isso sempre seria necessário ter todos os campos
class LivroUpdate(BaseModel):
	titulo:Optional[str] = Field(None, max_length=200)
	autor:Optional[str]= Field(None, min_length=3)
	ano_publicacao:Optional[int] = Field(None, gt=0)
	isbn:Optional[str] = Field(None,unique=True, min_length=13)
	disponivel:Optional[bool] = Field(None)

class LivroResponse(LivroBase):
	"""Schema para resposta ao usuario (deve incluir os campos do banco)"""
	id:int
	adicionado_em: datetime
	atualizado_em: datetime

	class Config:
		from_attributes = True  # Permite conversão de modelos SQLAlchemy


