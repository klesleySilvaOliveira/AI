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

int main(int argc, char const *argv[])
{
    List *li;
    Game matriz1, matriz2;
    li = list_create();

	int teste, i, j, k = 0;

	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			matriz1.matriz[i][j]=k;
			if(k == 8){
                matriz2.matriz[i][j]=0;
			}
			else{
                matriz2.matriz[i][j]=k+1;
			}
			k++;
		}
	}
	for(i = 0; i < 3; i++)
	{
		for(j = 0; j < 3; j++)
		{
			//printf("%d\n", matriz1.matriz[i][j]);
			printf("%d\n", matriz2.matriz[i][j]);
		}
	}
	matriz1.h=1;
	matriz2.h=2;
	teste = list_insert_sorted(li, matriz1);
	teste = list_insert_sorted(li, matriz2);
	teste = basica(&matriz1, matriz2);
	printf("\n%d", matriz1.h);
	teste = manhattan(&matriz1, matriz2);
	printf("\n%d", matriz1.h);
	return 0;
}
