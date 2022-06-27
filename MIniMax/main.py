# -*- coding: utf-8 -*-
from tabuleiro_velha import *

def add_velha(tabuleiro, valor, posicao):
	tabuleiro.matrix[posicao[0]][posicao[1]] = valor

def printar_tabuleiro():
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro.matrix[0][0]} │ {tabuleiro.matrix[0][1]} │ {tabuleiro.matrix[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[1][0]} │ {tabuleiro.matrix[1][1]} │ {tabuleiro.matrix[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[2][0]} │ {tabuleiro.matrix[2][1]} │ {tabuleiro.matrix[2][2]} │")
    print("└───┴───┴───┘")

def verificar_termino():
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

printar_tabuleiro()
print("Houve vencedor? "+verificar_termino()) #printa quem ganhou X ou O...