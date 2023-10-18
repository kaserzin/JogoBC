from inimigo import NPC


class Armas_Foice_Machado_Espada(NPC):

  def __init__(self):
    super().__init__()
    self._nomes_armas = ['Foice', 'Machado', 'Espada'] ##definindo o nome do foice;
    self._dano_foice = 8  #definindo o dano do foice;
    self._peso_foice = 0.1  #definindo o peso do foice;
    self._dano_machado = 17  #definindo o dano do machado;
    self._peso_machado = 0.2  #definindo o peso do machado;
    self._dano_espada = 25  #definindo o dano da espada;
    self._peso_espada = 0.3  #definindo o peso da espada;

  def Ataque_Foice(
      self, inimigo):  # Adiciona o parâmetro "inimigo" para afetar o NPC alvo.
    if inimigo.vivo:
      inimigo.vida -= self._dano_foice
      print('''_/﹋\_
(҂`_´) –
<;︻╦╤─ ҉ – – – – – – – – – – – – –''')
      if inimigo.morreu():
        return inimigo.morreu()
      else:
        return f"Inimigo após o ataque: Vida =  {inimigo.vida}"
    else:
      return "O inimigo está morto!"

  def Ataque_Machado(
      self, inimigo):  # Adiciona o parâmetro "inimigo" para afetar o NPC alvo.
    if inimigo.vivo:
      inimigo.vida -= self._dano_machado
      print('''_/﹋\_
(҂`_´) –
<;︻╦╤─ ҉ – – – – – – – – – – – – –''')
      if inimigo.morreu():
        return inimigo.morreu()
      else:
        return f"Inimigo após o ataque: Vida =  {inimigo.vida}"
    else:
      return "O inimigo está morto!"

  def Ataque_Espada(
      self, inimigo):  # Adiciona o parâmetro "inimigo" para afetar o NPC alvo.
    if inimigo.vivo:
      inimigo.vida -= self._dano_espada
      print('''_/﹋\_
(҂`_´) –
<;︻╦╤─ ҉ – – – – – – – – – – – – –''')
      if inimigo.morreu():
        return inimigo.morreu()
      else:
        return f"Inimigo após o ataque: Vida =  {inimigo.vida}"
    else:
      return "O inimigo está morto!"


# Consider this snippet from ./inimigo.py:
# from random import randint
#
#
# class NPC():
#   def __init__(self):
#     self.NPC_vida = randint(20, 101)
#     self.NPC_vivo = True
#
#   def morreu(self):
#     if self.NPC_vida <= 0:
#       self.NPC_vivo = False
#       return True
#
