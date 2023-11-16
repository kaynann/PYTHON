# alguns cuidados com dados mutáveis
# mutavel - na programação são dados que podem ter seu valor alterado na memória do dispositivo
# imutavel - são dados que só pdem ser copiados da memória do dispostivo
# copy - método que copia o valor de outra lista em outro endereço de memória

lista = ['João', 'Paulo']
lista[1] = "José"
print(lista)

nome = 'Paulo'
novo_nome = nome
nome = "João"
print(nome)
print(novo_nome)

lista_a = ["Kaynan", "Junior"]
print(lista_a)
lista_b = lista_a
lista_b[1] = "Coelho"
print(lista_a)
print(lista_b)
