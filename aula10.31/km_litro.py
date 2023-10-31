km = float(input("Quantos Km foi seu percurso?"))
litro = float(input("Quantos litros seu carro consumiu?"))

km_litro = km / litro

if km_litro < 8:
  print("Venda o carro")
elif km_litro >= 8 and km_litro <= 14:
  print("Econômico")
elif km_litro > 14:
  print("Super econômico")
else: 
  print("Consumo não encontrado")