# faça um codigo que leia 5 números e informe o maior número. 

contador = 1
lista_number = []
while contador <= 5:
  number = int(input('Digite um numero: '))
  lista_number.append(number)
  contador += 1
print(lista_number)
print(f'O maior número digitado foi: {max(lista_number)}')