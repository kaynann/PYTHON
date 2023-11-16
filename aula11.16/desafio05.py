nomes_lista = []
for i in range(1, 6):
  nomes = input('Digite um nome: ')
  nomes_lista.append(nomes)

  if nomes[0] == 'A' or nomes[0] == 'E' or nomes[0] == 'I' or nomes[0] == 'O' or nomes[0] == 'U': 
    print("Seu nome inicia com uma vogal")
  elif nomes[0] == 'a' or nomes[0] == 'e' or nomes[0] == 'i' or nomes[0] == 'o' or nomes[0] == 'u': 
    print("Seu nome inicia com uma vogal")
del nomes_lista[2]
print(nomes_lista)