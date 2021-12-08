"""
    Mundo tamanho 8x8
    Robô começa em 1,1
"""
from sillywalk import *

# tabuleiro vazio com tamanho aleatório
Mundo(largura=random.randint(3,8), altura=random.randint(3,8), ladrilho=40)
Robot(1, 1)