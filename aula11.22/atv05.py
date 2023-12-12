# Supondo que a população de um país A seja de 80000 habitantes com uma taxa anual de crescimento de 3% Faça um programa que calcule e escreva o número de anos necessários para que a população do país A chegar a 120000 habitantes

current_number = 80000
desired_number = 120000
growth_rate = 0.03

years = 0
while current_number < desired_number:
  current_number +=  current_number * growth_rate
  years += 1 
print(f'O total de anos para chegar na população desejada é { years } anos')