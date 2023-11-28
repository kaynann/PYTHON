# Faça um programa, com uma função que necessite de um argumento. A função retorna 'P', se seu argumento for positivo, e 'N' se for, se seu argumento for zero ou negativo

def verify(number):
  if number > 0:
    return 'P'
  elif number <= 0:
    return 'N'

user_number = int(input('Digite um número: '))
print(verify(user_number))