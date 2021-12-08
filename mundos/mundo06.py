"""
    Mundo 06
    Mundo tamanho 7,7
    barreiras nas linhas pares
    sempre tem um buraco num lugar aleatório
    ir de 1,1 até 7,7
"""
from sillywalk import *
import random

# desenha o tabuleiro
Mundo(largura=7, altura=7, ladrilho=40)
Robot(1, 1)

# faz três linhas
for i in range(1,4): # conta 1,2,3
  # sorteia o lugar do buraco nessa linha]
  buraco = random.randint(1,7)
  # conta de 0 a 7
  for x in range(7):
    if x != buraco:
      # 1+x vai produzir 1,2,3,4,5,6,7 (1+0 até 1+6)
      # i*2 vai produzir 2,4,6 (1*2, 2*2 e 3*2)
      Parede(1+x, i*2)