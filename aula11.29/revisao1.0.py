'''variavel = 'A casa do kaynan é azul igual o céu'
print(variavel[-16:-12])
print(variavel[-3::])'''

# utilizando fatiamento e repetição imprima uma lista de "a" até o "e" removendo uma letra de cada vez 
lista = ['a', 'b', 'c', 'd', 'e']
for i in range(len(lista)):
  remove = lista[:5-i]
  print(remove)

