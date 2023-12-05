# dicionários: possuem chaves(KEYS) e valor(VALUES)
# parâmetro: {} ou dict()
# item dictionary: chave e valor. Ex: {{'user': 'kaynan'}
# dicionários são mutáveis
# chaves podem ser qualquer tipo de dado imutável
# keys() - retorna só as chaves
# values() - retorna só os valores
# items() - retorna chave e valor


person = {
  'nome': 'kaynan', 
  'sobrenome': 'junior' 
}

print(len(person))
print('=' * 40)

print(person.keys())# imprime só as chaves
print('=' * 40)

print(person.values()) # imprime só os valores
print('=' * 40)

for chave, valor in person.items(): #retorna chave e valor
  print(chave, valor)
print('=' * 40)

i = person.items() # retorna chave e valor
print(i)
print('=' * 40)

print(person['nome']) # imprimir uma chave específica
print('=' * 40)

d1 = {
  'valor1': 100,
  'valor2': 200,
  'valor3': 300, 
}

d2 = d1.copy()

print(d1)

d2['valor2'] = 600
print(d2)
print('=' * 40)

atualizar = {
  'valor4': 800,
  'valor5': 1000        
}

d1.update(atualizar) # atualizando o dicionário | OBS: NÃO SE PODE ATUALIZAR DICIONÁRIO COM OUTRO TIPO DE DADO A NÃO SER DICIONÁRIO
print(d1)