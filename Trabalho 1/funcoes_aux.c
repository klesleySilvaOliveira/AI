#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef LISTA_ENCADEADA_H_INCLUDED
#define LISTA_ENCADEADA_H_INCLUDED

#include "lista_encadeada.h"

#endif // LISTA_ENCADEADA_H_INCLUDED

#ifndef FUNCOES_AUX_INCLUDED
#define FUNCOES_AUX_INCLUDED

#include "funcoes_aux.h"

#endif // FUNCOES_AUX_INCLUDED
int maior(int num1, int num2){
    int maior, menor;
    if(num1 > num2){
        maior = num1;
        menor = num2;
    }
    else{
        maior = num2;
        menor = num1;
    }
    return maior-menor;
}

int compara_matriz(Game matriz1, Game matriz2){
    int i, j;
    for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			if(matriz1.matriz[i][j] != matriz2.matriz[i][j]){
               return 0;
			}
		}
	}
	return 1;
}

int find_pos(Game game, int numero, int *i, int *j){
    int k, l;
    for(k = 0; k < 3; k++)
	{
		for(l = 0; l < 3; l++)
		{
			if(game.matriz[k][l] == numero){
                *i = k;
                *j = l;
                return 1;
			}
		}
	}
    return 0;
}

int arround(Game game, int *top, int *right, int *down, int *left){
    int teste, i, j;
    teste = find_pos(game, 0, &i, &j);
    *top = *right = *down = *left = 1;
    if(teste){
        if(i <= 0){                  //top
            *top = 0;
        }
        if(i >= 2){                  //down
            *down = 0;
        }
        if(j <= 0){                  //left
            *left = 0;
        }
        if(j >= 2){                  //right
            *right = 0;
        }
    }
    else{
        return 0;   //error
    }
    return 1;       //success
}

int get_g(Game *game){
    return game->g;
}

void set_g(Game *game, int g){
    game->g = g;
}

int get_h(Game *game){
    return game->h;
}

void set_char(Game *game, char c){
    game->pai[game->g] = c;
}

char get_char(Game *game, int pos){
    return game->pai[pos];
}

void print_matrix(Game game){
    int i, j;
    printf("\n");
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            if(j == 0){
                printf("|");
            }
            printf(" %d ",game.matriz[i][j]);
            if(j == 2){
                printf("|\n");
            }
        }
    }
}

void print_pais(Game origem, Game destino){
    int i, j, k, teste;
    for(i = 1; i <= get_g(&destino); i++){
        print_matrix(origem);
        if(destino.pai[i] == 't'){
            teste = find_pos(origem, 0, &j, &k);
            origem.matriz[j][k] = origem.matriz[j - 1][k];
            origem.matriz[j - 1][k] = 0;
        } else if(destino.pai[i] == 'r'){
            teste = find_pos(origem, 0, &j, &k);
            origem.matriz[j][k] = origem.matriz[j][k + 1];
            origem.matriz[j][k + 1] = 0;
        } else if(destino.pai[i] == 'd'){
            teste = find_pos(origem, 0, &j, &k);
            origem.matriz[j][k] = origem.matriz[j + 1][k];
            origem.matriz[j + 1][k] = 0;
        }else if(destino.pai[i] == 'l'){
            teste = find_pos(origem, 0, &j, &k);
            origem.matriz[j][k] = origem.matriz[j][k - 1];
            origem.matriz[j][k - 1] = 0;
        }
    }
    print_matrix(origem);
}
