"""
    Mundo 01
    Mundo tamanho 8x8
    Robô começa em 1,1
    Uma barreira vertical de altura aleatório e largura aleatória
    A barreira começa sempre na linha 2 e nunca passa da linha 7
    A barreira pode estar na coluna 2 até a 7
    (ou seja: a barreira é sempre transponível)
"""
from sillywalk import *

# desenha o tabuleiro
Mundo(largura=8, altura=8)
Robot(1, 1)

#barreira
minX = random.randint(2, 6)
maxX = random.randint(minX+1, 7)
minY = 2
maxY = random.randint(minY, 7)
for y in range(minY, maxY+1):
    for x in range(minX, maxX+1):
        Parede(x, y)