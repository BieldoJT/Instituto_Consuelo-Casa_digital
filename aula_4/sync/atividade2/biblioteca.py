from livro import Livro
import re

class Biblioteca:

	def __init__(self):
		self.lista_livros = []

	def adicionar_livro(self, titulo, autor, ano):
		new_livro = Livro(titulo, autor, ano)
		self.lista_livros.append(new_livro)

	def buscar_por_autor(self, nome):
		if re.search(r"[0-9]", nome) or not isinstance(nome, str):
			raise TypeError("Coloque um nome válido")
		lista = []
		for livro in self.lista_livros:
			if livro.autor == nome:
				livro.printar_info()
				lista.append(livro)
		return lista


	def listar_todos(self):
		return self.lista_livros

	def printar_todos(self):
		for livro in self.lista_livros:
			livro.printar_info()

	def retornar_lista_todos(self):
		lista = []
		for livro in self.lista_livros:
			lista.append(livro)
		return lista

