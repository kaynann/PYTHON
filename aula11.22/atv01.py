# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de núemros ímpares

# Usando List comprehensions
numbers = [int(input(f'Digite o número: '))for i in range(1, 11)]

pares = [pairs for pairs in numbers if pairs % 2 == 0]
impares = [odd for odd in numbers if odd % 2 == 1]

print(f'Os números pares são { pares }')
print(f'Os números ímpares são { impares }')

'''
# Usando for e if da forma tradicional
pares2 = []
impares2 = []
for i in range(1, 11):
  num = int(input(f'Digite o { i }° número: '))
  if num % 2 == 0:
    pares2.append(num)
  else:
    impares2.append(num)
print(pares2)
print(impares2) '''
