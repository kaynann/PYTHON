name1 = input("Digite um nome: ")
name2 = input("Digite um nome: ")
name3 = input("Digite um nome: ")
name4 = input("Digite um nome: ")
name5 = input("Digite um nome: ")

lista_name = []

if name1[0] != 'A' and name1[0] != 'E' and name1[0] != 'I' and name1[0] != 'O' and name1[0] != 'U':
  print("Seu nome inicia com uma consoante") 

if name2[0] != 'A' and name2[0] != 'E' and name2[0] != 'I' and name2[0] != 'O' and name2[0] != 'U':
  print("Seu nome inicia com uma consoante") 

if name3[0] != 'A' and name3[0] != 'E' and name3[0] != 'I' and name3[0] != 'O' and name3[0] != 'U':
  print("Seu nome inicia com uma consoante") 

if name4[0] != 'A' and name4[0] != 'E' and name4[0] != 'I' and name4[0] != 'O' and name4[0] != 'U':
  print("Seu nome inicia com uma consoante") 

if name5[0] != 'A' and name5[0] != 'E' and name5[0] != 'I' and name5[0] != 'O' and name5[0] != 'U':
  print("Seu nome inicia com uma consoante")   

lista_name.insert(0, name2)
print(lista_name)