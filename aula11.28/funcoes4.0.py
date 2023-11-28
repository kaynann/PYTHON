# Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante,calcule e exibe a gorjeta do garçom, considerando 12% do valor da conta

def gorjeta(money):
  tip_waiter = money * 0.12
  return tip_waiter

account_restaurant = float(input('Digite o valor da conta: '))
print(f'A gorjeta do garçom fica R${ gorjeta(account_restaurant) }')