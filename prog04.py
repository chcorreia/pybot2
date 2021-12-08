""""
Mundo com tamanho aleatório
Robô começa em 1,1
Fazer zig-zag de cima para baixo até o fim
"""

from sillywalk import *
from mundos import mundo04

def zig():
  while not fora(direita):
    andar(direita)
  if not fora(abaixo):
    andar(abaixo)

def zag():    
    while not fora(esquerda):
      andar(esquerda)
    if not fora(abaixo):
      andar(abaixo)
  

#zigzag
while not fora(abaixo):
  zig()
  zag()

print("Viva!")