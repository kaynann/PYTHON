class Televisao:
  def __init__(self, tamanho, canal):
    self.tamanho = tamanho
    self.canal = canal
    self.ligada = False

  def ligar(self):
    self.ligada = True
    print('A Tv está ligada')
  
  def desligar(self):
    self.ligada = False
    print('A Tv está desligada')

  def get_tamanho(self):
    return self.tamanho
  
  def get_canal(self):
    if self.ligada == False:
       print('Ligue a Televisão para poder ver o canal.')
    else:
      if self.ligada == True:
       return self.canal

  def set_tamanho(self, novo_tamanho):
    self.tamanho = novo_tamanho

  def set_canal(self, novo_canal):
    if self.ligada == False:
       print('Ligue a Televisão para poder  mudar o canal.')
    else:
      if self.ligada == True:
        self.canal = novo_canal
        return self.canal
    

samsung_4k = Televisao('44 polegadas', 'SBT')
print(samsung_4k.get_tamanho())
samsung_4k.get_canal()
samsung_4k.ligar()
print(samsung_4k.get_canal())
samsung_4k.desligar()