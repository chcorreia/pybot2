"""
Mundo 8x8
Robô começa em 4,1
Duas barreiras verticais na coluna 3 e 5
Uma das duas tem um buraco.
Achar o buraco e fugir até a parede oposta
"""
from sillywalk import *

# desenha o tabuleiro
Mundo(largura=8, altura=8, ladrilho=40)
Vader(4, 1)
Trooper(3, 1)
Trooper(5, 1)

# sorteia se o buraco está na direita ou esquerda
lado = random.randint(1, 2)
# sorteia a altura do buraco
buraco = random.randint(2,8) 

# conta de 2 a 8 (não conta o 9)
for i in range(2, 9): 
  # parede da direita
  if i != buraco or lado == 2:
    Trooper(3, i)
  if i != buraco or lado == 1:
    Trooper(5, i)