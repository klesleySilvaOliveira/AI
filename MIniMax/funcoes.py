# -*- coding: utf-8 -*-
from tabuleiro_velha import *
import copy

def verifica_vazio(tabuleiro):
	for i in range(0, 3, 1):
		for j in range(0, 3, 1):
			if tabuleiro.matrix[i][j] == " ":
				return 1 #tem vazio
	return 0 #cheio

def add_velha(tabuleiro, valor, x, y):
	tabuleiro.matrix[x][y] = valor

def confere_validade(tabuleiro, x, y):
	if x < 0 or y < 0 or x > 2 or y > 2:
		return 0
	elif tabuleiro.matrix[x][y] == " ":
		return 1
	return 0

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
	if tabuleiro.matrix[0][0] == tabuleiro.matrix[1][0] == tabuleiro.matrix[2][0] != " ":
		return tabuleiro.matrix[0][0]
	elif tabuleiro.matrix[0][1] == tabuleiro.matrix[1][1] == tabuleiro.matrix[2][1] != " ":
		return tabuleiro.matrix[0][1]
	elif tabuleiro.matrix[0][2] == tabuleiro.matrix[1][2] == tabuleiro.matrix[2][2] != " ":
		return tabuleiro.matrix[0][2]

	# Verificar horizontais
	elif tabuleiro.matrix[0][0] == tabuleiro.matrix[0][1] == tabuleiro.matrix[0][2] != " ":
		return tabuleiro.matrix[0][0]
	elif tabuleiro.matrix[1][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[1][2] != " ":
		return tabuleiro.matrix[1][0]
	elif tabuleiro.matrix[2][0] == tabuleiro.matrix[2][1] == tabuleiro.matrix[2][2] != " ":
		return tabuleiro.matrix[2][0]

	# Verifica as 2 diagonais
	elif tabuleiro.matrix[0][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[2][2] != " ":
		return tabuleiro.matrix[0][0]
	elif tabuleiro.matrix[2][0] == tabuleiro.matrix[1][1] == tabuleiro.matrix[0][2] != " ":
		return tabuleiro.matrix[2][0]

	# Verifica empate
	elif not verifica_vazio(tabuleiro):
		return "empate"
	else:
		return "espaços vazios"

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
		return "O"
	else:
		return "X"

def maxi(tabuleiro):
	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	#melhor = -inf
	melhor = -10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "X"
				minimo = mini(estado)[1]
				if minimo > melhor:
					melhor = minimo
					melhor_movimento = copy.deepcopy(estado)
	
	return [melhor_movimento, melhor]

def mini(tabuleiro):
	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	#melhor = inf
	melhor = 10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "O"
				maximo = maxi(estado)[1]
				if maximo < melhor:
					melhor = maximo
					melhor_movimento = copy.deepcopy(estado)
	
	return [melhor_movimento, melhor]

def minimax(tabuleiro, player1, player2): #player = 1 for player 0 for CPU
	while verifica_vazio(tabuleiro):

		termino = verificar_termino(tabuleiro)

		if termino == "x" or termino == "X":
			return tabuleiro
		elif termino == "o" or termino == "O":
			return tabuleiro
		elif termino == "empate":
			return tabuleiro

		vez = verifica_vez(tabuleiro)
		printar_tabuleiro(tabuleiro)
		print("VEZ DO " + vez)

		if vez == "X":
			if player1:
				x = -1
				y = -1
				while x < 0 or y < 0 or x > 2 or y > 2:
					x, y = map(int, input("Enter two values: ").split())
					if not confere_validade(tabuleiro, x, y):
						x = -1
				add_velha(tabuleiro, "X", x, y)
			else:
				tabuleiro = maxi(tabuleiro)[0]
		elif vez == "O":
			if player2:
				x = -1
				y = -1
				while x < 0 or y < 0 or x > 2 or y > 2:
					x, y = map(int, input("Enter two values: ").split())
					if not confere_validade(tabuleiro, x, y):
						x = -1
				add_velha(tabuleiro, "O", x, y)
			else:
				tabuleiro = mini(tabuleiro)[0]

	return tabuleiro