#include <stdio.h>
#include <stdlib.h>

#ifndef LISTA_ENCADEADA_H_INCLUDED
#define LISTA_ENCADEADA_H_INCLUDED

#include "lista_encadeada.h"

#endif // LISTA_ENCADEADA_H_INCLUDED

#ifndef FUNCOES_AUX_INCLUDED
#define FUNCOES_AUX_INCLUDED

#include "funcoes_aux.h"

#endif // FUNCOES_AUX_INCLUDED
int maior(int num1, int num2){
    int diferenca, maior, menor;
    if(num1 > num2){
        maior = num1;
        menor = num2;
    }
    else{
        maior = num2;
        menor = num1;
    }
    diferenca = maior - menor;
    return diferenca;
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
