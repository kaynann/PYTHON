# criando classe
# a funcão padrão construtora do python é __init__
# devemos sempre usar o SELF nos objetos para dizer que é uma referência de si mesmo, ou seja, que pertence aquela classe, caso não use o self o python não saberá a quem pertence aquele objeto.

class Automovel:
  def __init__(self, placa, cor): # a função self referencia que pertence a classe
    self.placa = placa
    self.cor = cor

  def get_placa(self): # métodos
    return self.placa
  
  def get_cor(self):
    return self.cor
  
  def set_cor(self, nova_cor): # método pra alterar o valor de um atributo do objeto. (no caso aqui a cor)
    self.cor = nova_cor

  def dirigir(self, velocidade):
    print(f'Estou dirigindo a { velocidade }Km/h')

carro = Automovel('DHA-3568', 'Preto') # carro é uma instância de automovel
print(carro.get_placa(), carro.get_cor())
carro.dirigir(220)

carro.set_cor('Azul-escuro') # nova cor do carro
print(f'A nova cor do carro é: {carro.get_cor()}')


moto = Automovel('WEB-1510', 'Vermelha') # moto é uma instância de automovel
print(moto.get_placa(), moto.get_cor())
moto.dirigir(70)