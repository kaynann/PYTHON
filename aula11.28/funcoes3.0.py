# Faça um funçao que informe a quantidade de digitos de um determinado número inteiro
def size_number(number):
  size = len(number)
  return size

user_number = (input('Digite um número:'))
print(f'A quntidade de digitos do número { user_number } é: { size_number(user_number) }')