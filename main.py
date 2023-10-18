import sys
import os

from arma import Armas_Foice_Machado_Espada
from inimigo import NPC
from player import Player

#Ciando os objetos e definindo seus atributos
inimigo = NPC()
machado = Armas_Foice_Machado_Espada()
p = Player(velocidade=2, armadura=2)

print(f'\nPlayer: Vida = {p.vida}')  #Verificando a vida do Player
for i in range(10):
  print(
      inimigo.atacar(p)
  )  #Chamando o método atacar do objeto inimigo,fazendo-o atacar o player.

print(
    f"Arma_Foice: Dano da arma = {machado._dano_foice}\nArma_Machado: Dano da arma = {machado._dano_machado}\nArma_Espada: Dano da arma = {machado._dano_espada}\n"
)  #Veriicando o dano da arma do machado

print(f"Inimigo: Vida = {inimigo.vida}")  #Verificando a vida do Inimigo
print(machado.Ataque_Foice(inimigo))
print(machado.Ataque_Machado(inimigo))
print(
    machado.Ataque_Espada(inimigo)
)  #Chamando o método Ataque_Machado do objeto machado, fazendo-o atacar o inimigo.
print()
