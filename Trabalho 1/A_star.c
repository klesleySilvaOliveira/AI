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

int a_star(Game origem, Game destino, int tipo_heuristica){
    if(tipo_heuristica < 0 || tipo_heuristica > 1){
        printf("\nHeuristica errada. Somente 0 para Basica e 1 para Manhattan!");
        return 0;
    }

    List *open, *closed;
    int teste, top, right, down, left, aux, i, j;
    Game game1, game2;

    open = list_create();
    closed = list_create();

    if(tipo_heuristica){
        set_g(&origem, 0);
        teste = manhattan(&origem, destino);
    }
    else{
        set_g(&origem, 0);
        teste = basica(&origem, destino);
    }

    teste = list_insert_sorted(open, origem);

    if(teste == OUT_OF_MEMORY){
        printf("\nLista não encontrada!");
        return 0;
    }

    while(list_size(open)){
        list_front(open, &game1);
        teste = list_pop_front(open);
        if(teste != SUCCESS){
            printf("\nNao apagou\n");
        }
        if(compara_matriz(game1, destino)){
            printf("\nG: %d - H: %d", get_g(&game1), get_h(&game1));
            list_free(open);
            list_free(closed);
            return SUCCESS;
        }

        if(!(list_find(closed, game1))){
                teste = list_insert_sorted(closed, game1);

                teste = arround(game1, &top, &right, &down, &left);

                if(top){
                    printf("\ntop\n");
                    game2 = game1;
                    teste = find_pos(game2, 0, &i, &j);
                    if(!teste){
                      printf("\nValor 0 faltando!");
                      return 0;
                    };
                    game2.matriz[i][j] = game2.matriz[i - 1][j];
                    game2.matriz[i - 1][j] = 0;
                    aux = get_g(&game2);
                    set_g(&game2, ++aux);
                    if(tipo_heuristica){
                        teste = manhattan(&game2, destino);
                    }
                    else{
                        teste = basica(&game2, destino);
                    }
                    teste = list_insert_sorted(open, game2);
                }

                if(right){
                    printf("\nright\n");
                    game2 = game1;
                    teste = find_pos(game2, 0, &i, &j);
                    if(!teste){
                      printf("\nValor 0 faltando!");
                      return 0;
                    };
                    game2.matriz[i][j] = game2.matriz[i][j+1];
                    game2.matriz[i][j+1] = 0;
                    aux = get_g(&game2);
                    set_g(&game2, ++aux);
                    if(tipo_heuristica){
                        teste = manhattan(&game2, destino);
                    }
                    else{
                        teste = basica(&game2, destino);
                    }
                    teste = list_insert_sorted(open, game2);
                }

                if(down){
                    printf("\ndown\n");
                    game2 = game1;
                    teste = find_pos(game2, 0, &i, &j);
                    if(!teste){
                      printf("\nValor 0 faltando!");
                      return 0;
                    };
                    game2.matriz[i][j] = game2.matriz[i+1][j];
                    game2.matriz[i+1][j] = 0;
                    aux = get_g(&game2);
                    set_g(&game2, ++aux);
                    if(tipo_heuristica){
                        teste = manhattan(&game2, destino);
                    }
                    else{
                        teste = basica(&game2, destino);
                    }
                    teste = list_insert_sorted(open, game2);
                }

                if(left){
                    printf("\nleft\n");
                    game2 = game1;
                    teste = find_pos(game2, 0, &i, &j);
                    if(!teste){
                      printf("\nValor 0 faltando!");
                      return 0;
                    };
                    game2.matriz[i][j] = game2.matriz[i][j-1];
                    game2.matriz[i][j-1] = 0;
                    aux = get_g(&game2);
                    set_g(&game2, ++aux);
                    if(tipo_heuristica){
                        teste = manhattan(&game2, destino);
                    }
                    else{
                        teste = basica(&game2, destino);
                    }
                    teste = list_insert_sorted(open, game2);
                }

        }


        printf("\n\n tamanho: %d                                   tamanho: %d", list_size(open), list_size(closed));
        printf("\nt = %d - r = %d - d = %d - l = %d", top, right, down, left);
    }

    list_free(open);
    list_free(closed);

    return ELEM_NOT_FOUND;
}
