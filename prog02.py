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
from mundos import mundo02

# MISSÃO: CONTORNAR A BARREIRA PELA ESQUERDA E VOLTAR PARA A BORDA DIREITA

#andar a direita até detectar bloco 1 linha abaixo
while vazio(abaixo):
  andar(direita)
#andar a direita até não ter mais blocos
while not vazio(abaixo):
  andar(direita)
#se colocar em posição pra dar a segunda volta pra baixo
andar(abaixo)
#dar a volta pra baixo até não ter mais blocos
while not vazio(esquerda):
  andar(abaixo)
#andar até a esquerda e terminar o programa
while not fora (esquerda):
  andar(esquerda)

