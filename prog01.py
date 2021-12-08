"""
    Mundo 01
    Mundo tamanho 8x8
    Robô começa em 1,1
    Uma barreira vertical de altura aleatório com uma casa de largura
    A barreira começa sempre na linha 2 e nunca passa da linha 7
    A barreira pode estar na coluna 2 até a 7
    (ou seja: a barreira é sempre transponível)
"""
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

