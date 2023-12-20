class Pet:
  def __init__(self, nome, peso):
    self.nome = nome
    self.peso = peso
    self.fome = 0
    self.sede = 0
    self.comida = 100

  # GETs
  def get_nome(self):
    return self.nome
  
  def get_peso(self):
    return self.peso  

  def get_fome(self):
    return self.fome
  
  def get_sede(self):
    return self.sede 
  
  # SETs
  def set_nome(self, novo_nome):
    self.nome = novo_nome

  def set_peso(self, novo_peso):
    self.peso = novo_peso

  def set_fome(self, nova_fome):
    self.fome += nova_fome
    while self.fome >= 99:
      diferenca = self.fome - 99
      print(f'Você deve alimentar pelo menos {diferenca } de comida a/o { self.nome }')
      nova_comida = int(input('Quanto de comida você quer dá para eu pet? '))
      self.comida -= nova_comida
      self.fome -=  nova_comida
      self.peso -= 2

  def set_sede(self, nova_sede):
    self.sede = nova_sede

  def __str__(self):
    return f'Olá meu nome é: { self.nome }, estou pesando { self.peso }Kg, \n Minha fome está { self.fome }'
  
dog = Pet('Zeus', 50)
print(dog)
dog.set_fome(50)
print(dog)
dog.set_fome(60)
print(dog)