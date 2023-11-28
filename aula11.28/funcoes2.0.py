# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def reverse_number(number): 
  reverse = 0
  while number > 0:
    end_number = number % 10 # pegar o ultimo valor
    reverse = (reverse * 10) + end_number # adicionando na variável reverse
    number = number // 10
  return reverse
  
user_number = int((input('Digite um número: ')))
print(reverse_number(user_number))