
import pytest

from biblioteca import Biblioteca
from livro import Livro

def test_adicionar_livro():
	"Teste para validar o metodo de adição de livros na biblioteca"
	biblioteca = Biblioteca()
	biblioteca.adicionar_livro("O Cortiço", "Aluísio Azevedo", 1890)

	assert len(biblioteca.lista_livros) == 1
	assert isinstance(biblioteca.lista_livros[0], Livro)
	assert biblioteca.lista_livros[0].titulo == "O Cortiço"

def test_retornar_lista_todos():
	biblioteca = Biblioteca()
	biblioteca.adicionar_livro("Iracema", "José de Alencar", 1865)
	biblioteca.adicionar_livro("O Guarani", "José de Alencar", 1857)

	lista = biblioteca.retornar_lista_todos()
	assert len(lista) == 2
	for livro in lista:
		assert isinstance(livro, Livro)

def test_buscar_por_autor_e_encontrar():
	biblioteca = Biblioteca()
	biblioteca.adicionar_livro("Memórias Póstumas", "Machado de Assis", 1881)
	biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)

	lista = biblioteca.buscar_por_autor("Machado de Assis")

	assert lista[0].titulo == "Memórias Póstumas"
	assert lista[1].titulo == "Dom Casmurro"
	assert lista[0].autor and lista[1].autor == "Machado de Assis"

def test_buscar_por_autor_e_nao_encontrar():
	biblioteca = Biblioteca()
	biblioteca.adicionar_livro("Memórias Póstumas", "Machado de Assis", 1881)
	biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)

	lista = biblioteca.buscar_por_autor("Jorge Amado")

	assert len(lista) == 0

def test_adicionar_livro_tipos_invalidos():
	biblioteca = Biblioteca()

	#assim  da pra pegar apenas as mensagem de erro!!
	with pytest.raises(TypeError):
		biblioteca.adicionar_livro(4545, "Aldous Huxley", 1928)
	with pytest.raises(TypeError):
		biblioteca.adicionar_livro("Contraponto", "Aldous Huxley", "1928")
	with pytest.raises(TypeError):
		biblioteca.adicionar_livro("Contraponto", "Aldous 44y", 1928)
	with pytest.raises(TypeError):
		biblioteca.adicionar_livro("Contraponto", 4455, "1928")

def test_buscar_por_autor_nome_invalido():
	biblioteca = Biblioteca()
	biblioteca.adicionar_livro("Memórias Póstumas", "Machado de Assis", 1881)
	biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)


	with pytest.raises(TypeError):
		biblioteca.buscar_por_autor("Machado de 4ssis")
	with pytest.raises(TypeError):
		biblioteca.buscar_por_autor(455)

