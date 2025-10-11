"""Teste de senhas"""

from validador_senha import *




def test_senha_valida():
	"""Testa senhas Válidas"""
	senhas_validas = ["GbzinRd2025#",
				"Gui",
				"Lui$it00",
				"JHGHhgh232$$$"]
	for senha in senhas_validas:
			assert validar_senha(senha)
			print(f"A senha {senha}, deveria funcionar")

def test_senha_invalida():
	"""Teste que verifica senhas inválidas"""
	senhas_invalidas = ["Gabriel",
					 "Ga$2iel",
					 "GGGGGGGGG",
					 "ggggggggggg",
					 "GGaaaaaaaaaa",
					 "Ga2adadasdada",
					 "G%235435454354",
					 "____ççççaadasa"]
	for senha in senhas_invalidas:
		try:
			assert validar_senha(senha)
		except:
			print(f"A senha {senha},NÃo deveria funcionar")


