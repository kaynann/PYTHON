aluno = 1
while aluno <= 20:
  idade = int(input(f'Digite do aluno { aluno }: '))
  if idade > 13:
    print(f'A idade do aluno { aluno } é { idade }. E maior que 13.')
    aluno += 1