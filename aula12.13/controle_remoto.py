class ControleRemoto:
  def __init__(self, cor, tamanho, marca, qtd_pilhas):
    self.botoes = None
    self.cor = cor
    self.tamanho = tamanho
    self.marca = marca
    self.painel = False
    self.qtd_pilhas = qtd_pilhas
    

  def ligar(self):
    self.painel = True

  def desligar(self):
    self.painel = False

  def temperatura(self, nova_temp):
    if self.painel == False:
      print('Temperatura não pode ser alterada')
    self.temperatura = nova_temp

  def pressionar_botao(self, tipo_botao):
    self.botoes = tipo_botao
    if self.botoes == 'Ligar':
      self.ligar()

    elif self.botoes == 'Desligar':
      self.desligar()

controle = ControleRemoto('Branco', 'médio', 'elgin', 'duas')
controle.pressionar_botao('Ligar')
controle.temperatura(20)

