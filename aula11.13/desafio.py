# Crie uma lista com cinco nomes de alunos do curso de back-end.
#   a. imprima a lista
#   b. adicine um sexto nome na lista
#   c. remova o terceiro indice da lista 
#   d. remova um objeto especifico da lista
#   e. imprima a lista 
#   f. adicione um novo nome na lista

lista = ["Felipe", "Mikael", "Jefferson", "Geisa", "Wesley"]
print(lista)

lista.append("Elvis")
del lista[2]
lista.remove("Felipe")

print(lista)
lista.append("Kaynan")