#!/usr/bin/python3
import json

palavras = []
with open('texto.txt', 'r') as arquivo:
	for linha in arquivo:
		palavras.append(linha.strip())

total_palavras = 0
palavras_grandes = 0
my_dict = dict(total_palavras = 0, palavras_grandes = 0, porcentagem = 0)


for linha in palavras:
	my_dict["total_palavras"] += 1
	if len(linha) > 5:
		my_dict["palavras_grandes"] +=1

total_palavras = my_dict["total_palavras"]
palavras_grandes = my_dict["palavras_grandes"]
my_dict["porcentagem"] = (palavras_grandes/total_palavras)*100



dados = json.dumps(my_dict)

print(dados)



# usar with ja ajuda a abrir e fechar o arquivo automaticamente
# sem a necessidade de close
