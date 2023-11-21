# for trabalha com iteráveis !!!
# tem que possuir uma variável de controle
# iter() - transforma um objeto em iterável
# next() - 

nome = 'Kaynan'
texto = iter(nome)
print(texto)

'''for letra in nome:
 print(letra)'''

# enumerate() - é um iterador de indices e valores

lista = ['João', 'Pedro', 'Mateus', 'Judas', 'Tiago']
print(lista)
lista_enumerada = enumerate(lista)
print(list(lista_enumerada))

for item in lista_enumerada:
  print(item)