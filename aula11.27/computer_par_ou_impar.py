from random import randint

placar_jogador = 0
placar_computador = 0

while True:
  jogador = (input('Escolhar par ou ímpar: ')).lower()
  
  jogador_number = int(input('Digite um número: '))
  computer_number = randint(0, 10)

  result = jogador_number + computer_number
  print(f'O número do computador foi: { computer_number }')
  
  if result % 2 == 0:
    if jogador == 'par':
      placar_jogador += 1
      print('Jogador ganhou!!!')
    else:
      placar_computador += 1
      print('Computador ganhou!!!')
  else:
    if jogador == 'impar':
      placar_jogador += 1
      print('Jogador ganhou!!!')
    else:
      placar_computador += 1
      print('Computador ganhou!!!')
  print(f'PLACAR => Jogador: { placar_jogador } | Computador: { placar_computador }')

  saida = input('Digite [s] parar sair ou [c] para continuar: ').lower()
  
  if saida == 's':
    if placar_computador > placar_jogador:
      confirma_saida = input('Você ta perdendo. Vai arregar? Frango! Digite "coco" para sair ou "c" para continuar: ')
      if confirma_saida == 'coco':
        print('FRANGO')
        break
      else:
        continue
    elif placar_jogador > placar_computador:
      print('\nVocê venceu!!!')
      break 
    elif placar_computador == placar_jogador:
      print('Placar empatadado!')
      break