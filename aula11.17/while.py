contador = 0
while contador < 300:
  contador += 1     # é o mesmo que contador = contador + 1
  print(contador)
  if contador == 12:
    print("Cheguei no 12")
  if contador == 290:
    break
print("Saiu do while")
