import re

def validar_qtd_caracteres(str):
	if len(str) < 8:
		raise ValueError("A senha deve ter mais de 8 Caracteres")
	else:
		return

def validar_letra_maiuscula(str):
	maiuscula = r"[A-Z]"
	resultado = re.search(maiuscula, str)
	if resultado:
		return
	else:
		raise ValueError("Não tem letra maiuscula")

def validar_letra_minuscula(str):
	minuscula = r"[a-z]"
	resultado = re.search(minuscula, str)
	if resultado:
		return
	else:
		raise ValueError("Não tem letra minuscula")

def validar_numeros(str):
	numeros = r"[0-9]"
	resultado = re.search(numeros, str)
	if resultado:
		return
	else:
		raise ValueError("Não tem numeros")

def validar_caracter_especial(str):
	especial = r"\W|_|ç|Ç"
	resultado = re.search(especial, str)
	if resultado:
		return
	else:
		raise ValueError("Não tem caracter especial")

def validar_senha(senha):
	try:
		validar_qtd_caracteres(senha)
		validar_letra_maiuscula(senha)
		validar_letra_minuscula(senha)
		validar_numeros(senha)
		validar_caracter_especial(senha)
	except:
		raise ValueError("qurbrou")

