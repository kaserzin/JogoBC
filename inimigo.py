from random import randint


class NPC():

  def __init__(self):
    self.__NPC_vida = randint(20, 100)
    self.__NPC_vivo = True
    self.__NPC_ataque = randint(10, 20)

  def atacar(self, jogador):
    if jogador.vivo:
      jogador.vida -= self.ataque
      if jogador.morreu():
        return jogador.morreu()
      else:
        return f"O inimigo te atacou e te deu {self.ataque} de dano\nPlayer após o ataque: Vida =  {jogador.vida}"

  def morreu(self):
    if self.vida <= 0:
      self.vivo = False
      self.vida = 0
      return """
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀── 
O inimigo morreu!"""
    else:
      return False

  #getters
  @property
  def vida(self):
    return self.__NPC_vida

  @vida.setter
  def vida(self, new_vida):
    self.__NPC_vida = new_vida

  @property
  def vivo(self):
    return self.__NPC_vivo

  @vivo.setter
  def vivo(self, new_vivo):
    self.__NPC_vivo = new_vivo

  @property
  def ataque(self):
    return self.__NPC_ataque
