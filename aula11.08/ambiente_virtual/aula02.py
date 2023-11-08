entrada = input('[E] para entra e [S] para passar: ')
senha_digitada = input('Digite a senha de acesso: ')
senha = '12345678'

if (entrada == 'E' or entrada == 'e'):
  if (senha == senha_digitada):
    print("Sucesso, você entrou")
  else:
    print("Senha incorreta")
elif(entrada == 'S' or entrada == 's'):
  if(senha == senha_digitada):
    print("Sucesso, você passou")
  else:
    print("Senha incorreta")
else:
  print("Você não selecionou uma opção válida")  