#include <stdio.h>
#include <stdlib.h>

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
    List *open, *closed;
    Game matriz1, matriz2;

    open = list_create();
    closed = list_create();

	int teste, i, j, k = 0, t, r, d, l;

	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			matriz1.matriz[i][j]=k;
		}
	}
	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			printf("\nValor %d %d: ", i, j);
			scanf("%d", &matriz1.matriz[i][j]);
		}
	}
	matriz2.matriz[0][0] =
	matriz2.matriz[1][1]=10;
	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{

			//printf("%d\n", matriz1.matriz[i][j]);
			//printf("%d\n", matriz2.matriz[i][j]);
		}
	}
	matriz1.h=1;
	matriz2.h=2;
	teste = list_insert_sorted(open, matriz1);
	teste = basica(&matriz1, matriz2);
	printf("\n%d", matriz1.h);
	teste = manhattan(&matriz1, matriz2);
	printf("\n%d", matriz1.h);
	teste = list_find(open, matriz2);
	printf("\n%d", teste);
	teste = find_pos(matriz1, 1, &i, &j);
	printf("\n%d", i);
	printf("\n%d", j);
	teste = arround(matriz1, &t, &r, &d, &l);
	printf("\ntop: %d", t);
	printf("\nright: %d", r);
	printf("\ndown: %d", d);
	printf("\nleft: %d", l);
	teste = a_star(matriz1, matriz2, 1);
	return 0;
}
