import re
class Livro:
	"""classe livro"""

	'''Esse é o metodo construtor, sempre é executado quando um novo objeto é criado'''
	def __init__(self, titulo, autor, ano):
		#Esses são os atributos da classe instanciada
		if not isinstance(titulo, str):
			raise TypeError("Coloque um titulo deve ser uma string")
		if re.search(r"[0-9]", autor):
			raise TypeError("Coloque um nome válido")
		if not isinstance(ano, int) and ano > 0:
			raise TypeError("O ano deve ser um inteiro positivo")
		self.titulo = titulo
		self.autor = autor
		self.ano = ano

	"""Esse é um metodo da classe, aqui ele retorna uma string com as informações do livro instanciado"""
	def __str__(self):
		return f"{self.titulo},{self.autor},{self.ano}"

	def printar_info(self):
		print(f"titulo: {self.titulo}, autor: {self.autor}, ano: {self.ano}")

	def listar_info(self):
		lista = []
		lista.append(self.titulo)
		lista.append(self.autor)
		lista.append(self.ano)
		return lista
