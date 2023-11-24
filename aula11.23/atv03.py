user_name = input("Digite um nome: ")

vogal_a = 'a'

for i in vogal_a:
  user_name = user_name.replace(vogal_a, '')
  

print(f'Seu nome sem vogais fica: { user_name }')