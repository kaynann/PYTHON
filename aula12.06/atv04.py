# Crie um cadastro de clientes recebendo nome, idade e endereço completo. Adicione todas as informações em um dicionário. Imprima no final.

user_name = input('Digite seu nome: ')
user_year = int(input('Digite sua idade: '))
user_birth = input('Digite sua data de aniversário: ')
user_road= input('Digite o nome da sua rua: ')
user_residence_number = input('Digite o número da sua residência: ')
user_bairro = input('Digite o nome do seu bairro: ')

dic_client = {
  'nome': user_name,
  'idade': user_year,
  'data de nascimento': user_birth,
  'rua': user_road,
  'número da residência': user_residence_number,
  'bairro': user_bairro,
}

print(dic_client)