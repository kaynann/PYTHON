# faça um codigo que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e pedindo as informações novamente.

while True:
  user_name = input('Digite seu nome: ')
  user_password = input('Digite uma senha: ')
  if user_password == user_name:
    print("ERRO! Sua senha não pode ser igual seu nome. Insira os dados novamente.")
  else:
    break