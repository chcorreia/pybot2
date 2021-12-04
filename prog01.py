from sillywalk import *
from mundos import mundo01

# MISSÃO: CONTORNAR A BARREIRA PELA ESQUERDA E VOLTAR PARA A BORDA DIREITA

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

