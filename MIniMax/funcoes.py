# -*- coding: utf-8 -*-
from tabuleiro_velha import *
from numpy import inf
import copy

def add_velha(tabuleiro, valor, posicao):
	tabuleiro.matrix[posicao[0]][posicao[1]] = valor

def printar_tabuleiro(tabuleiro):
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro.matrix[0][0]} │ {tabuleiro.matrix[0][1]} │ {tabuleiro.matrix[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[1][0]} │ {tabuleiro.matrix[1][1]} │ {tabuleiro.matrix[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[2][0]} │ {tabuleiro.matrix[2][1]} │ {tabuleiro.matrix[2][2]} │")
    print("└───┴───┴───┘")

def verificar_termino(tabuleiro):
    # Verificar verticais
    if tabuleiro.matrix[0][0] == tabuleiro.matrix[1][0] == tabuleiro.matrix[2][0] != ' ':
        return tabuleiro.matrix[0][0]
    elif tabuleiro.matrix[0][1] == tabuleiro.matrix[1][1] == tabuleiro.matrix[2][1] != ' ':
        return tabuleiro.matrix[0][1]
    elif tabuleiro.matrix[0][2] == tabuleiro.matrix[1][2] == tabuleiro.matrix[2][2] != ' ':
        return tabuleiro.matrix[2][0]

	# Verificar horizontais
    elif tabuleiro.matrix[0][0] == tabuleiro.matrix[0][1] == tabuleiro.matrix[0][2] != ' ':
        return tabuleiro.matrix[0][0]
    elif tabuleiro.matrix[1][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[1][2] != ' ':
        return tabuleiro.matrix[1][0]
    elif tabuleiro.matrix[2][0] == tabuleiro.matrix[2][1] == tabuleiro.matrix[2][2] != ' ':
        return tabuleiro.matrix[2][0]

    # Verifica as 2 diagonais
    elif tabuleiro.matrix[0][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[2][2] != ' ':
        return tabuleiro.matrix[0][0]
    elif tabuleiro.matrix[2][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[0][2] != ' ':
        return tabuleiro.matrix[2][0]

    # Verifica empate
    elif [*tabuleiro.matrix].count(' ') == 0:
        return "empate"
    else:
        return 0

def verifica_vazio(tabuleiro):
	for i in range(0, 3, 1):
		for j in range(0, 3, 1):
			if tabuleiro.matrix[i][j] == "":
				return 1
	return 0

def verifica_vez(tabuleiro):
	x = 0
	o = 0
	for i in range(0, 3, 1):
		for j in range(0, 3, 1):
			if tabuleiro.matrix[i][j] == "X" or tabuleiro.matrix[i][j] == "x":
				x += 1
			elif tabuleiro.matrix[i][j] == "O" or tabuleiro.matrix[i][j] == "o":
				o += 1
	if x > o:
		return "X"
	else:
		return "O"

def maxi(tabuleiro):
	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	melhor = -inf
	#melhor = -10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == "":
				estado.matrix[x][y] = "X"
				minimo = mini(estado)[1]
				if minimo > melhor:
					melhor = minimo
					melhor_movimento = copy.deepcopy(estado)
	
	return [melhor_movimento ,melhor]

def mini(tabuleiro):
	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	melhor = inf
	#melhor = 10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == "":
				estado.matrix[x][y] = "O"
				maximo = maxi(estado)[1]
				if maximo < melhor:
					melhor = maximo
					melhor_movimento = copy.deepcopy(estado)
	
	return [melhor_movimento ,melhor]

def minimax():
	pass