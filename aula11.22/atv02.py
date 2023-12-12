# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
maior = 0
menor = None
while True:
  number = int(input('Digite um número: '))
  saida = input('Digite [S] para sair ou [C] para continuar: ').upper()

  if number > maior:
    maior = number
  if menor == None or number < menor:
    menor = number 
  if saida == 'S':
    break
  else:
    continue
print(f'O maior número é: { maior }. E o menor número é { menor }. E a soma dos dois é igual a: { menor + maior }')