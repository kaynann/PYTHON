# faça um código que crie uma lista com 20 números inteiros e armazene os números pares na lista pares e os números impares na lista impar, imprima as duas listas.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_impar = numbers[0::2]
lista_par = numbers[1::2]

print(f'Números ímpares { lista_impar }')
print(f'Números pares { lista_par }')