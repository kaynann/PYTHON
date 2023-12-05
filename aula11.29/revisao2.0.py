# estruturas condicionais
variavel = 20
if variavel > 20:
  print('+20')
elif variavel == 20:
  print('=20')
else:
  print('-20')

# estruturas de repetição
# FOR E WHILE
for i in range(1, 10, 2):
  print(f'print o número { i }')

contador = 5
while contador > 0:
  print(f'Número { contador }')
  contador -=1

# join - unir strings
lista = ['12', '01', '2023']
nome = '/'.join(lista[::-1])
print(nome)