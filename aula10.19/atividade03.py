# variáveis de input recebendo um valor inserido pelo usuário
salario = float(input("Informe seu salário atual: "))
reajuste = float(input("Informe a porcentagem do reajuste: "))

# variáveis de que calculam a porcentagem do salario e o novo salário do usuário
valor_aumento = salario * reajuste / 100
novo_salario = salario + valor_aumento

print(f'O seu novo salário é R$ {novo_salario}')  