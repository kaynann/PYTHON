# count - a função dele é contar quantas vezes um determinado caractere aparece em uma string
# upper - deixa a string toda maiúscula
# lower - deixa a string roda minúscula
# find - busca por uma expressão dentro da frase
# replace - faz alterações dentro da string
# capitalize - deixa a primeira letra da string maiúscula
# split - transforma a string em uma lista

frase = " A banana é amarela e o abacate é verde".lower()
letra = "a"

print(f'A letra "{ letra }" aparece {frase.count(letra)} vezes na frase "{ frase }"')

achei = frase.find('rela')

if achei >= 0:
  print(f'A expressão foi encontrada no indíce: { achei }')
else:
  print('Expressão não encontrada')

nova_frase = frase.replace('banana', 'maracujá') # <-- como se usa o replace
print(nova_frase)

frase2 = "o rato roeu a roupa do rei de roma".capitalize()
print(frase2)
print(frase2.split())