number01 = int(input('Digite um número: '))
number02 = int(input('Digite um número: '))

if number01 > number02:
  number01, number02 = number02, number01

for i in range(number01 + 1, number02):
  print(i)