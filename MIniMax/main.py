# -*- coding: utf-8 -*-
from tabuleiro_velha import *
from funcoes import *

tabuleiro = velha()

tabuleiro = minimax_ab(tabuleiro, 0, 0)
printar_tabuleiro(tabuleiro)
print("Houve vencedor? "+verificar_termino(tabuleiro)) #printa quem ganhou X ou O...