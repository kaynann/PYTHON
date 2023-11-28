# Funções - são blocos de códigos que são executados somente quando são chamadas. Parâmetro: def
def media (nota1, nota2, nota3):
  media = nota1 + nota2 + nota3
  return media

for i in range(1,4):
  nota = input(f'Digite a nota { i }: ')
media(nota[0], nota[1], nota [2])
print(f'A média é: { media }')