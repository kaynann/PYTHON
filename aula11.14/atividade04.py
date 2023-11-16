#  faça um codigo que pede 5 letras e quando for consoante ele avisa é uma consoante

lista_consoantes = []
letra_1 = input("Digite uma letra: ")
letra_2 = input("Digite uma letra: ")
letra_3 = input("Digite uma letra: ")
letra_4 = input("Digite uma letra: ")
letra_5 = input("Digite uma letra: ")

if (letra_1 != 'a' and letra_1 != 'e' and letra_1 != 'i' and letra_1 != 'o' and letra_1 != 'u'):
    lista_consoantes.append(letra_1)

if (letra_2 != 'a' and letra_2 != 'e' and letra_2 != 'i' and letra_2 != 'o' and letra_2 != 'u'):
    lista_consoantes.append(letra_2)
 
if (letra_3 != 'a' and letra_3 != 'e' and letra_3 != 'i' and letra_3 != 'o' and letra_3 != 'u'):
    lista_consoantes.append(letra_3)

if (letra_4 != 'a' and letra_4 != 'e' and letra_4 != 'i' and letra_4 != 'o' and letra_4 != 'u'):
    lista_consoantes.append(letra_4)
 
if (letra_5 != 'a' and letra_5 != 'e' and letra_5 != 'i' and letra_5 != 'o' and letra_5 != 'u'):
    lista_consoantes.append(letra_5)

print(f'As letras consoantes são { lista_consoantes }')