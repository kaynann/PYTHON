#input de que pedem para o usuário informar um número inteiro
number1 = input("Informe um primeiro número inteiro: ")
number2 = input("Informe o segundo número inteiro: ")
number3 = input("Informe o terceiro número inteiro: ")

# execução da primeiro cálculo pedido na questão
product = ((int(number1) * 2) * (int(number2) / 2)) + int(number3)
print(int(product))

# execução do segundo cálculo pedido na questão
soma = (int(number1) * 3 + int(number3)) * int(number2) 
print(soma)