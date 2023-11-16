# Lista são um conjunto de elementos
# extend - método que estende uma lista, junta ela com outra
 
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

lista_c = lista_a + lista_b #juntar listas - concatenar | o sinal de + aqui está praticando POLIMORFISMO

print(lista_c, type(lista_c))

lista_a.extend(lista_b) # o valor estendido será adicionado na variável lista_a
print(lista_a) 