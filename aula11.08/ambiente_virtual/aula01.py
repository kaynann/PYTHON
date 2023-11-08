nome = 'Kaynan Junior'
altura = 1.65
peso = 60
imc = peso / (altura ** 2)

# A resposta dessa questão deve ser:
# Fulano tem ALT de altura, pesa PES quilo e seu IMC é:
# valor

print(nome, ' tem ', altura, ' de altura,')
print('pesa ', peso, ' quilos e seu IMC é: ')
print(imc)

print(f'{nome} tem {altura} de altura, pesa, {peso}, quilos e seu IMC é:')
print(f'{imc:.2f}')