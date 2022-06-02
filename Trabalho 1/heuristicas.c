#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef LISTA_ENCADEADA_H_INCLUDED
#define LISTA_ENCADEADA_H_INCLUDED

#include "lista_encadeada.h"

#endif // LISTA_ENCADEADA_H_INCLUDED

#ifndef HEURISTICAS_H_INCLUDED
#define HEURISTICAS_H_INCLUDED

#include "heuristicas.h"

#endif // HEURISTICAS_H_INCLUDED

#ifndef FUNCOES_AUX_INCLUDED
#define FUNCOES_AUX_INCLUDED

#include "funcoes_aux.h"

#endif // FUNCOES_AUX_INCLUDED

int basica(Game *game, Game objetivo){
    int i, j, aux=0;
    for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			if((*game).matriz[i][j] != objetivo.matriz[i][j]){
                aux++;
			}
		}
	}
	(*game).h=aux;
    return 0;
}

int manhattan(Game *game, Game objetivo){
    int i, j, k, l, aux=0, col, row;
    for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			for(k = 0; k < 3; k++)
            {
                for(l = 0; l < 3; l++)
                {
                    if((*game).matriz[i][j] == objetivo.matriz[k][l]){
                        col = maior(i, k);
                        row = maior(j, l);
                        aux = aux + col + row;
                        l = 3;
                    }
                }
            }
		}
	}
	(*game).h=aux;
    return 0;
}
