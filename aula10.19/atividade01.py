# variavel input pedindo um valor ao usuario
temperatura = input("Informe a temparatura em °F: ")

# conversao do valor inserido pelo usuario em °F
convert = 5 * ((int(temperatura) - 32) / 9)

print(f'A temperatura equivale a: {int(convert)}°C')