# -*- coding: utf-8 -*-

class velha:
	def __init__(self):
		self.matrix = ([" "," "," "],[" "," "," "],[" "," "," "])

def exibir_tabuleiro():
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro.matrix[0][0]} │ {tabuleiro.matrix[0][1]} │ {tabuleiro.matrix[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[1][0]} │ {tabuleiro.matrix[1][1]} │ {tabuleiro.matrix[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro.matrix[2][0]} │ {tabuleiro.matrix[2][1]} │ {tabuleiro.matrix[2][2]} │")
    print("└───┴───┴───┘")