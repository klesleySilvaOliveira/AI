# -*- coding: utf-8 -*-
from tabuleiro_velha import *
import copy

maxx = 0
minn = 0

#Confere se há algum espaço vazio na matriz. 1 para sim e 0 para não
def verifica_vazio(tabuleiro):
	for i in range(0, 3, 1):
		for j in range(0, 3, 1):
			if tabuleiro.matrix[i][j] == " ":
				return 1 #tem vazio
	return 0 #cheio

#Adiciona o valor informado nas posições informadas
def add_velha(tabuleiro, valor, x, y):
	tabuleiro.matrix[x][y] = valor

#REcebe 2 matrizes e retorna uma lista com as posições que diferem nas matrizes
def tip(tabuleiro1, tabuleiro2):
	lista = []
	for i in range(0, 3, 1):
		for j in range(0, 3, 1):
			if tabuleiro1.matrix[i][j] != tabuleiro2.matrix[i][j]:
				lista.append(i)
				lista.append(j)
	return lista

#Confere se os valores informados estão no intervalo de disponibilidade da matriz informada
def confere_validade(tabuleiro, x, y):
	if x < 0 or y < 0 or x > 2 or y > 2:
		return 0
	elif tabuleiro.matrix[x][y] == " ":
		return 1
	return 0

#Imprime o tabuleiro de forma padronizada
def printar_tabuleiro(tabuleiro):
	print("┌───┬───┬───┐")
	print(f"│ {tabuleiro.matrix[0][0]} │ {tabuleiro.matrix[0][1]} │ {tabuleiro.matrix[0][2]} │")
	print("├───┼───┼───┤")
	print(f"│ {tabuleiro.matrix[1][0]} │ {tabuleiro.matrix[1][1]} │ {tabuleiro.matrix[1][2]} │")
	print("├───┼───┼───┤")
	print(f"│ {tabuleiro.matrix[2][0]} │ {tabuleiro.matrix[2][1]} │ {tabuleiro.matrix[2][2]} │")
	print("└───┴───┴───┘")

#Verifica as condições de término e retorna o vencedor ou empate
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

#verifica a quantidade de cada elemento na matriz para definir de quem é a vez
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
	#Soma quantas vezes MAXI foi realizado
	global maxx
	maxx += 1

	#Verifica o termino e adiciona o valor na variável 'termino'
	termino = verificar_termino(tabuleiro)

	#REaliza testes de finalidade na variável teste, para finalizar a recursão retornando 1 para vitoria do MAX, -1 para vitória do MIN e 0 para empate
	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	#Cria as variáveis melhor e melhor_movimento, que contém o melhor resultado e o melhor movimento, respectivamente
	melhor = -10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			#Faz uma cópia total do tabuleiro informado para uma variável que possa ser alterada
			estado = copy.deepcopy(tabuleiro)
			#Adiciona o movimento em cada um dos espaços disponíveis e chama a recursão de acordo com o movimento alcançado
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "X"
				maximo = mini(estado)[1]
				#Se o valor resgatado na recursão for maior que o valor presente na variável 'melhor', 'melhor' recebe o valor da recursão e 'melhor_movimento' recebe o estado copiado
				if maximo > melhor:
					melhor = maximo
					melhor_movimento = copy.deepcopy(estado)

	#REtorna o melhor movimento e o resultado final projetado
	return [melhor_movimento, melhor]

def mini(tabuleiro):
	#Soma quantas vezes MINI foi realizado
	global minn
	minn += 1
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
				minimo = maxi(estado)[1]
				if minimo < melhor:
					melhor = minimo
					melhor_movimento = copy.deepcopy(estado)
	
	return [melhor_movimento, melhor]

def minimax(tabuleiro, player1, player2): #player = 1 for player 0 for CPU
	#REsgata as variáveis globais MAXX e MINN
	global maxx
	global minn

	#Cria o vetor vazio que receberá as dicas
	dica = []

	#Verifica de quem é a vez e adiciona na variável
	vez = verifica_vez(tabuleiro)

	#Enquanto o tabuleiro possui espaços vazios...
	while verifica_vazio(tabuleiro):

		#Verifica término
		termino = verificar_termino(tabuleiro)

		if termino == "x" or termino == "X":
			return tabuleiro
		elif termino == "o" or termino == "O":
			return tabuleiro
		elif termino == "empate":
			return tabuleiro

		#Imprime o tabuleiro atual e de quem é a vez
		printar_tabuleiro(tabuleiro)
		print("VEZ DO " + vez)

		#Vez do X
		if vez == "X":			
			#Se a variável player1, informada no cabeçalho, for 1 (é jogador ativo)...
			if player1:
				#Declara 2 variáveis responsáveis pela posição informada pelo jogador
				x = -1
				y = -1

				#REcebe uma dica de jogada ao enviar o tabuleiro atual e o tabuleiro alcançado por 'maxi' e imprime a dica
				dica = tip(tabuleiro, maxi(tabuleiro)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				#Enquanto os valores x e y não forem válidos...
				while not confere_validade(tabuleiro, x, y):
					#REcebe valores separados por vírgula e adiciona às variáveis x e y
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())

				#Adiciona a jogada informada pelo usuário no tabuleiro
				add_velha(tabuleiro, "X", x, y)

			#Caso não seja jogador ativo...
			else:
				#...IA irá jogar
				tabuleiro = maxi(tabuleiro)[0]

			#Altera a variável 'vez' para o valor 'O'
			vez = "O"

		#Vez do X
		elif vez == "O":
			#Se a variável player2, informada no cabeçalho, for 1 (é jogador ativo)...
			if player2:
				x = -1
				y = -1

				#REcebe uma dica de jogada ao enviar o tabuleiro atual e o tabuleiro alcançado por 'mini' e imprime a dica
				dica = tip(tabuleiro, mini(tabuleiro)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				while not confere_validade(tabuleiro, x, y):
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())

				add_velha(tabuleiro, "O", x, y)
			else:
				tabuleiro = mini(tabuleiro)[0]

			#Altera a variável 'vez' para o valor 'X'
			vez = "X"

	#REtorna o tabuleiro finalizado e as quantidades iteradas de MAXX e MINN
	return [tabuleiro, maxx, minn]

def maxi_otm(tabuleiro):
	global maxx
	maxx += 1

	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	melhor = -10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "X"
				maximo = mini_otm(estado)[1]
				if maximo > melhor:
					melhor = maximo
					melhor_movimento = copy.deepcopy(estado)
				#Como 1 é o maior valor possível para 'maxi_otm', e o 'maximo' sempre será o primeiro maior número resgatado, na ocorrência de 1, o algoritmo já finaliza
				if maximo == 1:
					return [melhor_movimento, melhor]
	
	return [melhor_movimento, melhor]

def mini_otm(tabuleiro):
	global minn
	minn += 1

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
				minimo = maxi_otm(estado)[1]
				if minimo < melhor:
					melhor = minimo
					melhor_movimento = copy.deepcopy(estado)
				#Como -1 é o menor valor possível para 'mini_otm', e o 'minimo' sempre será o primeiro menor número resgatado, na ocorrência de -1, o algoritmo já finaliza
				if minimo == -1:
					return [melhor_movimento, melhor]
	
	return [melhor_movimento, melhor]

def minimax_otm(tabuleiro, player1, player2): #player = 1 for player 0 for CPU
	global maxx
	global minn
	dica = []

	vez = verifica_vez(tabuleiro)

	while verifica_vazio(tabuleiro):

		termino = verificar_termino(tabuleiro)

		if termino == "x" or termino == "X":
			return tabuleiro
		elif termino == "o" or termino == "O":
			return tabuleiro
		elif termino == "empate":
			return tabuleiro

		printar_tabuleiro(tabuleiro)
		print("VEZ DO " + vez)

		if vez == "X":
			if player1:
				x = -1
				y = -1

				dica = tip(tabuleiro, maxi_otm(tabuleiro)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				while not confere_validade(tabuleiro, x, y):
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())
				
				add_velha(tabuleiro, "X", x, y)
			else:
				tabuleiro = maxi_otm(tabuleiro)[0]

			vez = "O"

		elif vez == "O":
			if player2:
				x = -1
				y = -1

				dica = tip(tabuleiro, mini_otm(tabuleiro)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				while not confere_validade(tabuleiro, x, y):
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())
				
				add_velha(tabuleiro, "O", x, y)

			else:
				tabuleiro = mini_otm(tabuleiro)[0]

			vez = "X"

	return [tabuleiro, maxx, minn]

def maxi_alfa(tabuleiro, alfa, beta):
	global maxx
	maxx += 1

	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	melhor = -10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "X"
				maximo = mini_beta(estado, alfa, beta)[1]
				
				if maximo > melhor:
					melhor = maximo
					melhor_movimento = copy.deepcopy(estado)
				
				#Se o valor calculado for maior ou igual a beta, finaliza o algoritmo
				if maximo >= beta:
					return [melhor_movimento, melhor]
				
				#Se o melhor valor calculado for maior que o alfa, alfa recebe o melhor valor
				if melhor > alfa:
					alfa = melhor
	
	return [melhor_movimento, melhor]

def mini_beta(tabuleiro, alfa, beta):
	global minn
	minn += 1

	termino = verificar_termino(tabuleiro)

	if termino == "x" or termino == "X":
		return [tabuleiro, 1]
	elif termino == "o" or termino == "O":
		return [tabuleiro, -1]
	elif termino == "empate":
		return [tabuleiro, 0]

	melhor = 10
	melhor_movimento = copy.deepcopy(tabuleiro)

	for x in range(0, 3, 1):
		for y in range(0, 3, 1):
			estado = copy.deepcopy(tabuleiro)
			if estado.matrix[x][y] == " ":
				estado.matrix[x][y] = "O"
				minimo = maxi_alfa(estado, alfa, beta)[1]

				if minimo < melhor:
					melhor = minimo
					melhor_movimento = copy.deepcopy(estado)

				#Se o valor calculado for menor ou igual a alfa, finaliza o algoritmo
				if minimo <= alfa:
					return [melhor_movimento, melhor]

				#Se o melhor valor calculado for menor que o beta, beta recebe o melhor valor
				if melhor < beta:
					beta = melhor
	return [melhor_movimento, melhor]

def minimax_alfa_beta(tabuleiro, player1, player2): #player = 1 for player 0 for CPU
	global maxx
	global minn

	dica = []

	vez = verifica_vez(tabuleiro)

	while verifica_vazio(tabuleiro):

		termino = verificar_termino(tabuleiro)

		if termino == "x" or termino == "X":
			return tabuleiro
		elif termino == "o" or termino == "O":
			return tabuleiro
		elif termino == "empate":
			return tabuleiro

		
		printar_tabuleiro(tabuleiro)
		print("VEZ DO " + vez)

		if vez == "X":
			if player1:
				x = -1
				y = -1

				dica = tip(tabuleiro, maxi_alfa(tabuleiro, -10, 10)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				while not confere_validade(tabuleiro, x, y):
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())

				add_velha(tabuleiro, "X", x, y)

			else:
				tabuleiro = maxi_alfa(tabuleiro, -10, 10)[0]

			vez = "O"

		elif vez == "O":
			if player2:
				x = -1
				y = -1

				dica = tip(tabuleiro, mini_beta(tabuleiro, -10, 10)[0])
				print("Dica de melhor jogada: " + str(dica[0]) + " e " + str(dica[1]))

				while not confere_validade(tabuleiro, x, y):
					x, y = map(int, input("Informe as posições válidas desejadas (0 ~ 2) separadas por espaço: ").split())

				add_velha(tabuleiro, "O", x, y)

			else:
				tabuleiro = mini_beta(tabuleiro, -10, 10)[0]

			vez = "X"

	return [tabuleiro, maxx, minn]