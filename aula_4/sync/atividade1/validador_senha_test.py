"""Teste de senhas"""
import pytest
from validador_senha import *




def test_senha_valida():
	"""Testa senhas Válidas"""
	senhas_validas = ["GbzinRd2025#",
				"GuiRdela22@Bia",
				"Lui$it00",
				"JHGHhgh232$$$"]
	for senha in senhas_validas:
		assert validar_senha(senha) == True

def test_senha_invalida():
	"""Teste que verifica senhas inválidas"""
	senhas_invalidas = ["Gabriel",
					 "Ga$2iel",
					 "GGGGGGGGG",
					 "aslkhalfjhsdfskj",
					 "GGaaaaaaaaaa",
					 "Ga2adadasdada",
					 "G%235435454354",
					 "____ççççaadasa"]
	for senha in senhas_invalidas:
		assert validar_senha(senha) == False



