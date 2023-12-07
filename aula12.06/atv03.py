# 3. faça um codigo que pede a marca e o modelo do carro do cliente insere ele em uma lista e depois transforma em um dicionario. Imprima os dois resultados.
lista_de_carros = []
dic_carros = {}
marca = input('Informe a marca do seu carro: ')
modelo = input('Informe o modelo do seu carro: ')

lista_de_carros.append(marca)
lista_de_carros.append(modelo)

dic_carros.update([lista_de_carros])
print(lista_de_carros)
print(dic_carros)
