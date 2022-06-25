# -*- coding: utf-8 -*-
from tabuleiro_velha import *

def add_velha(tabuleiro, valor, posicao):
	tabuleiro.matrix[posicao[0]][posicao[1]] = valor

tup = [1, 2]
tabuleiro = velha()
lista = list(tup)
print(type(lista))
print(lista[0])
add_velha(tabuleiro, 'X', lista)
print(tabuleiro.matrix[1][2])