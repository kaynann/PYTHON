# variavel com input pedindo um valor para o usuário
user_height = input("Informe sua altura em metros(Ex: 1.50): ")

# variáveis que calculam o peso ideal com base no valor inserido pelo usuário
weight_man = (72.7 * float(user_height)) -58
weight_girl = (62.1 * float(user_height)) - 44.7

print(f'Se você for homem, seu peso ideal é: {float(weight_man)} Kg')
print(f'Se você for mulher, seu peso ideal é: {float(weight_girl)} Kg')