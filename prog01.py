from sillywalk import *

# desenha o tabuleiro
Mundo(largura=8, altura=8, ladrilho=40)
Robot(1, 1)
#barreira de peões
x = random.randint(3, 7)
minY = 2
maxY = random.randint(minY+1,7)
for y in range(minY, maxY+1):
    Parede(x, y)

# programa do aluno

#andar a direita até achar o bloqueio na linha de baixo
while vazio(abaixo):
   andar(direita)

#dar uma volta no bloqueio
andar(direita)
andar(abaixo)
while not vazio(esquerda):
  andar(abaixo)

#continuar a andar a esquerda
while not fora(esquerda):
   andar(esquerda)

#parar de andar na borda

