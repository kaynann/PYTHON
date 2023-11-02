n = input('Digite algo: ')

print(f'O dado é do tipo: {type(n)}')

print(f'É alfabético? {n.isalpha()}') 
print(f'É numérico? {n.isnumeric()}')
print(f'É espaço? {n.isspace()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minusculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
