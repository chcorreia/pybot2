"""
    Mundo tamanho 8,8
    Estalactites descendo do teto entre 2 e 7
    fazer o morcego seguir o contorno do teto
    ir de 1,1 até 1,8
"""
from sillywalk import *
import random

Mundo(8,8, ladrilho=40)
Objeto("morcego.png", 1, 1)

# conta de 2 a 7
for x in range(2,8):
  # altura da estalactite
  altura = random.randint(2,7)
  # repete "altura" vezes
  for y in range(altura):
    Objeto("rochas.png", x, y)