# condição ternária acontece em formato de linha
salário = float(input('Digite seu salário: '))
if salário >= 2500.00:
  print("IR será cobrado")
else:
  print("IR não será cobrado")

variavel_controle = 'IR será cobrado!' if salário >= 2500 else 'IR não será cobrado!'
print(variavel_controle)

var_control = 'OK 1' if True else 'OK 2' if False else 'Fim'
print(var_control)