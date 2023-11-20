# faça um codigo que peça uma nota, entre zero e dez. Mostre uma mensagem caso a nota seja inválida e continue pedindo até que o usuário informe uma nota válida.

while True:
  nota = float(input('Digite uma nota entre 0 e 10: '))
  if nota < 0 or nota > 10:
    print("Nota inválida!")
  elif nota >= 0 and nota <= 10:
    print("Nota válida!")
    break