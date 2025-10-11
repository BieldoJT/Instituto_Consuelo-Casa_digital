#!/usr/bin/python3

import pandas as pd
import math



def media_alunos(df):
	media_alunos = {}
	for i in range(0,9):
		linha = df.loc[i]
		nome = linha.iloc[0]
		nota1 = linha.iloc[1]
		nota2 = linha.iloc[2]
		nota3 = linha.iloc[3]
		media_alunos[nome] = (math.ceil((nota1 + nota2 + nota3)/3))
	return media_alunos


df =pd.read_csv("alunos.csv")
media = media_alunos(df)
print(media)







#media_alunos(df)

#quando eu assim:
#print(a[1])

#da esse erro:
# FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels
# (consistent with DataFrame behavior).
# To access a value by position, use `ser.iloc[pos]`

#devo usar iloc para pegar pelo indice e não o nome da posição






