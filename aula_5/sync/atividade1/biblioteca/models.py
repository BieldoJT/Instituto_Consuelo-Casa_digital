from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from biblioteca.database import Base

class Livro(Base):

	__tablename__="livros"

	id = Column(primary_key=True, autoincrement=True)
	titulo = Column(String(200),nullable=False)
	autor = Column(String(100), nullable=False)
	ano_publicacao = Column(Integer, nullable=False)
	isbn = Column(String(50), nullable=False)
	disponivel = Column(Boolean, nullable=False)

	# Timestamps automáticos
	adicionado_em = Column(DateTime(timezone=True), server_default=func.now())
	atualizado_em = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

	def __repr__(self):
		return f"<livro(id={self.id}, titulo={self.titulo}, ano={self.ano_publicacao})>"



