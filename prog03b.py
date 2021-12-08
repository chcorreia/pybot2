""""
Mundo 8x8
Robô começa em 1,1
Fazer zig-zag de cima para baixo até o fim
"""

from sillywalk import *
from mundos import mundo03

# compare essa rotina com os do prog03
def zigzag(direcao):
  while not fora(direcao):
    andar(direcao)
  if not fora(abaixo):
    andar(abaixo)
  

# faz o zigzag
while not fora(abaixo):
  zig(direita)
  zag(esquerda)

print("Viva!")