# -*- coding: utf-8 -*-
from tabuleiro_velha import *
from funcoes import *

tup = [0, 0]
tabuleiro = velha()
lista = list(tup)
#print(type(lista))
#print(lista[0])
add_velha(tabuleiro, 'X', lista)
print(tabuleiro.matrix[1][2])
tabuleiro.matrix[1][2] = 'O'
tabuleiro.matrix[0][2] = 'X'
tabuleiro.matrix[0][1] = 'O'
tabuleiro.matrix[2][0] = 'X'
tabuleiro.matrix[1][0] = 'O'
tabuleiro.matrix[1][1] = 'X'
tabuleiro.matrix[2][1] = 'O'
tabuleiro.matrix[2][2] = 'X'

printar_tabuleiro(tabuleiro)
print("Houve vencedor? "+verificar_termino(tabuleiro)) #printa quem ganhou X ou O...