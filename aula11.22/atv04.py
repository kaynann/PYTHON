# Faça um programa que peça para 10 pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, dizer se a turma é jovem ou adulta ou idosa, conforme a média calculada 

ages = []
for i in range(10):
  user_age = int(input(f'Digite a { i + 1 }º idade: '))
  ages.append(user_age)

young = sum(ages) / len(ages)
adult = sum(ages) / len(ages)
elderly = sum(ages) / len(ages)

if young >= 0 and young <= 25:
  print(f'Turma jovem')
elif adult >= 26 and adult <= 60:
  print('Turma adulta')
elif elderly > 60:
  print('Turma idosa')