# Operadores IN e NOT IN
seu_nome = input("Informe seu nome: ")
buscar = input("Informe o valor a ser encontrado: ")

if (buscar in seu_nome):
  print(f'{ buscar } está dentro de { seu_nome }')
else:
  print(f'O valor não esta inserido em { seu_nome }')