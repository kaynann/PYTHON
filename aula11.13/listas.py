# uma - lista é representada pelos []
# len - metódo que retorna a quantidade de itens de uma lista
# append - metódo que atualiza valores no fim da lista
# del - metódo que remove item pelo indice especifico da lista
# remove - metódo que remove um objeto especificado da lista
# pop - metódo que  remove o último onjeto da sua lista
# insert - método que adiciona um objeto em qualquer local da lista

lista  = []
print(lista, type(lista))
print(len(lista))

lista = ["Front"]
print(lista, type(lista))
print(len(lista))

lista = ["Back"]
print(lista, type(lista))
print(len(lista))

lista.append('Front')
print(lista, type(lista))
print(len(lista))

lista = ["Back", "Tarde", 21, True, 8.8]
print(f'A quantidade de alunos da turma é: {lista[2]}')
lista[2] = 22
print(lista)

lista[1] = False
print(lista)

lista[1] = ["Neyva", "Alice", "Lara", "Paula", "Geisa", "Felipe"]
print(lista)
print(lista[1][2])

lista[1][2] = "Kaynan"
print(lista)

print(lista[-2])
del lista[-2]
print(lista[-2])

lista.remove("Back")
print(lista)

lista.append(990)
lista.append(10)
print(lista)
valor_do_pop = lista.pop()
print(lista)
print(f'O cliente removido foi do ID: { valor_do_pop }')

lista.insert(0, "Amontada Valley")
print(lista)

lista.insert(2, "Paulo")
print(lista)