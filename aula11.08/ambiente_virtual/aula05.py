# Fatiamento de strings
# OBS: toda string por padrão que não saiu do armário
# ordem de tratamento
# 12345678........
# -87654321.......
# [i:f:p] = i - INICIO, f - FIM, p - PARSE

nome = "Rodrigo Jose dos Santos Amaral Neto Junior"
print(nome[17:23])
print(nome[-6:])
print(nome[0::2]) #par
print(nome[1::2]) #ímpar

lista_nome = ("K", "a", "y", "n", "a", "n")

print("=" * 20)
print(nome[3]) 
print(nome[-2])

print(lista_nome[3]) 
print(lista_nome[-2])