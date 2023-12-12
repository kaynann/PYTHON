# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
number = int(input('Digite um número: '))
if number > 1:
  for i in range(2, number // 2 + 1):
    print(i)
    if number % i == 0:
      print('Este número não é primo')
      break
  else:
    print(f'Este número é primo')
else:    
   print('Este número não  é primo')