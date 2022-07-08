# -*- coding: utf-8 -*-
from tabuleiro_velha import *
from funcoes import *
import time

tabuleiro = velha()
fim_de_jogo = []
jogo = -1
jogador1 = -1
jogador2 = -1

while(jogo < 0 or jogo > 2):
	jogo = int(input("> 0 - MiniMax comum\n> 1 - MiniMax otimizado\n> 2 - MiniMax Alfa-Beta\n> Informe a opção: "))

while(jogador1 < 0 or jogador1 > 1 or jogador2 < 0 or jogador2 > 1):
	print("\nJogador X:\n")
	jogador1 = int(input("> 0 - IA\n> 1 - JOGADOR\n> Informe a opção: "))
	print("\nJogador O:\n")
	jogador2 = int(input("> 0 - IA\n> 1 - JOGADOR\n> Informe a opção: "))


# get the start time
st = time.time()

if jogo == 0:
	fim_de_jogo = minimax(tabuleiro, jogador1, jogador2)
elif jogo == 1:
	fim_de_jogo = minimax_otm(tabuleiro, jogador1, jogador2)
else:
	fim_de_jogo = minimax_alfa_beta(tabuleiro, jogador1, jogador2)

printar_tabuleiro(fim_de_jogo[0])
print("Houve vencedor? " + verificar_termino(fim_de_jogo[0])) #printa quem ganhou X ou O...
print("Foram realizadas ", fim_de_jogo[1]," iterações de MAX e ", fim_de_jogo[2], " iterações de MIN.")

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Tempo de execução:', elapsed_time, 'segundos')