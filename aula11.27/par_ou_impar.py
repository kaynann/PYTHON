jogador1 = input("Escolha par ou impar: ").lower()

if jogador1 == 'par':
  jogador2 = 'impar'
else:
  jogador2 = 'par'

jogador1_number = int(input('Digite um número: '))
jogador2_number = int(input('Digite um número: '))

resultado = jogador1_number + jogador2_number

if resultado % 2 == 0:
  if jogador1 == 'par':
    print('Jogador 1. You Win!!!')
  else: 
    print('Jogador 2. You Win!!!')
else:
  if jogador1 == 'impar':
    print('Jogador 1. You Win!!!')
  else: 
    print('Jogador 2. You Win!!!')