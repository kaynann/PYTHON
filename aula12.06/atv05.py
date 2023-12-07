# 5. vamos criar um sistema de login e senha. crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. em seguida peça as informações e valide o login do usuario


login_senha = {
  'kaynan': 1234,
  'felipe': 5678,
}

acesso = {}
user_name = input('Digite seu login: ')
user_pass = int(input('Digite sua senha: '))

acesso = {user_name: user_pass}


for chave in login_senha.keys():
    if login_senha[chave] == acesso[user_name]:
      if chave == user_name:
        print('Acesso liberado')
        break
else:
   print('Acesso negado!')
