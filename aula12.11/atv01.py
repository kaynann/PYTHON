def verify_word(user_word):
  while len(user_word) < 3:
    print('A palavra deve conter três ou mais caracteres')
    user_word = input('Digite novamente: ').upper()
  return user_word

def verify_index(words, prhase):
  index_found = []

  for word in words:
    if word in prhase:
      index_initial = prhase.index(word)
      index_end = index_initial + len(word) - 1
      index_found.append((word, index_initial, index_end))
  return index_found
 
# palavra 01  
user_word01 = input('Digite a primeira palavra: ').upper()
user_word01 = verify_word(user_word01)

# palavra 02
user_word02 = input('Digite a segunda palavra: ').upper()
user_word02 = verify_word(user_word02)

# palavra 03
user_word03 = input('Digite a terceira palavra: ').upper()
user_word03 = verify_word(user_word03)

list_word = [user_word01, user_word02, user_word03]

# input de frase e validação
user_phrase = input('Digite um frase: ').upper()
if len(user_phrase) < 20:
  print('A frase deve conter 20 ou mais caracteres.')
  user_phrase = input('Digite a frase novamente: ')

print(user_phrase)

results = verify_index(list_word, user_phrase)
print()

if results:
  for i, r in enumerate(results, start=1):
    print(f'A palavra { i } foi encontrada no intervalo de indices: { r }') 
else:
  print('As palavras não estão na frase')