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

#ifndef A_STAR_INCLUDED
#define A_STAR_INCLUDED

#include "A_star.h"

#endif // A_STAR_INCLUDED

int main(int argc, char const *argv[])
{
    Game matriz, matriz2;
    int teste, i, j, heuristica;

    printf("Informe a Matriz origem: \n");
	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			printf("\nValor %d %d: ", i, j);
			scanf("%d", &matriz.matriz[i][j]);
		}
	}

	printf("\nInforme a Matriz destino: \n");

	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			printf("\nValor %d %d: ", i, j);
			scanf("%d", &matriz2.matriz[i][j]);
		}
	}

    printf("\nInforme a Heuristica(0 - Basica ou 1 - Manhattan): \n");
    scanf("%d", &heuristica);

	teste = a_star(matriz, matriz2, heuristica);

	if(teste == SUCCESS){
        printf("\nSolucao encontrada!!");
	}
	else{
        printf("\nSolucao nao encontrada!");
	}

	return 0;
}
