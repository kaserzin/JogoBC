#Definindo a classe Pocao
class Pocao:
  #Definindo o construtor da classe
  def __init__(self):
    self.__nome_pocao = 'pocao'
    self.__possivel_coletar = False

  @property
  def nome(self):
    return self.__nome_pocao

  @property
  def possivel_coletar(self):
    return self.__possivel_coletar

  @possivel_coletar.setter
  def possivel_coletar(self, novo_valor):
    self.__possivel_coletar = novo_valor