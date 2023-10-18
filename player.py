from pocao import Pocao
from arma import Armas_Foice_Machado_Espada as Armas


class Player(Pocao, Armas):

  def __init__(self, velocidade, armadura):
    super().__init__()
    self.__player_velocidade = 8
    self.__player_vida = 100
    self.__player_vivo = True
    self._player_armas = []
    self._player_armadura = armadura
    self._player_inventario = []

  def usar_pocao(self):
    inv = self._player_inventario
    if len(inv) == 0:
      return 'Você não tem poção'
    for item in inv:
      if item == 'pocao':
        self.vida += 10
        return f'''Utilizando poção...
  ─▄█▀█▄──▄███▄─
  ▐█░██████████▌
  ─██▒█████████─
  ──▀████████▀──
  ─────▀██▀─────-
Você agora tem: {self.vida} de vida'''
        inv.remove('pocao')

  def coletar_pocao(self):
    self._player_inventario.append('pocao')
    return f'Você coletou uma poção e agora tem: {self._player_inventario}'

  def morreu(self):
    if self.vida <= 0:
      self.vivo = False
      self.vida = 0
      raise SystemExit(
          Exception("""
      █████████
      █▄█████▄█
      █▼▼▼▼▼
      █
      GAME OVER!!!
      █▲▲▲▲▲
      █████████
      ██ ██
      \nFIM DE JOGO!!
      """))
    else:
      return False

  def coletar_arma(self, nome_arma):
    # Verifique se a arma já está no inventário
    if nome_arma in self._player_inventario:
        return f"Você já possui a arma {nome_arma} no inventário."
    else:
        # Adicione a arma ao inventário
        self._player_inventario.append(nome_arma)
        return f"Você coletou a arma {nome_arma} e agora ela está no seu inventário."

  def equipar_arma(self, nome_arma):
    # Verifique se o jogador tem a arma no inventário
    if nome_arma in self._player_inventario:
      # Equipar a arma selecionada
      self._player_armas.append(nome_arma)
      # Remover a arma do inventário
      self._player_inventario.remove(nome_arma)

      return f"Você equipou a arma {nome_arma}"
    else:
      return f"Você não tem a arma {nome_arma} no inventário. Colete a arma antes de equipá-la."

  #getters
  @property
  def velocidade(self):
    return self.__player_velocidade

  @property
  def vida(self):
    return self.__player_vida

  @vida.setter
  def vida(self, new_vida):
    self.__player_vida = new_vida

  @property
  def vivo(self):
    return self.__player_vivo

  @vivo.setter
  def vivo(self, new_vivo):
    self.__player_vivo = new_vivo
