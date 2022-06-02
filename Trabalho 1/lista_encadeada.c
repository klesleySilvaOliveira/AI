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

typedef struct list_node List_node;
typedef struct list List;

struct list{
    List_node *head;
};

struct list_node{
    Game data;
    List_node *next;
};

List* list_create(){
    List *li;

    li = (List *)malloc(sizeof(List));

    if(li != NULL){
        li->head = NULL;
    }

    return li;
}

int list_free(List *li){

    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    List_node *aux, *aux2;
    aux = li->head;
    while(aux != NULL){
        aux2 = aux->next;
        free(aux);
        aux = aux2;
    }
    free(li);
    return SUCCESS;
}

int list_push_front(List *li, Game game){

    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    List_node *a;
    a = (List_node *)malloc(sizeof(List_node));
    if(a == NULL){
        return OUT_OF_MEMORY;
    }
    a->data = game;
    a->next = li->head;
    li->head = a;

    return SUCCESS;
}

int list_size(List *li){
    int aux;
    List_node *a;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }

    a = li->head;
    aux = 0;

    while(a != NULL){
        a = a->next;
        aux++;
    }

    return aux;
}

int list_pop_front(List *li){
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    if(li->head == NULL){
        return INVALID_NULL_POINTER;
    }
    List_node *aux;
    aux = li->head->next;
    free(li->head);
    li->head = aux;
    return SUCCESS;
}

int list_front(List *li, Game *game){
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    if(li->head == NULL){
        return INVALID_NULL_POINTER;
    }
    *game = li->head->data;
    return SUCCESS;
}

int list_insert_sorted(List *li, Game game){
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
        if(list_size (li) == 0 || (game.h + game.g) < (li->head->data.h + li->head->data.g)){
        list_push_front(li, game);
        return SUCCESS;
    }
    List_node *aux, *a;
    a = (List_node *)malloc(sizeof(List_node));
    aux = li->head;

    if(a == NULL){
        return OUT_OF_MEMORY;
    }

    a->data = game;

    while(aux != NULL){
        if((game.h + game.g) >= (aux->data.h + aux->data.g) && aux->next == NULL){
            aux->next = a;
            a->next = NULL;
            return SUCCESS;
        }else if((game.h + game.g) >= (aux->data.h + aux->data.g) && (game.h + game.g) < (aux->next->data.h + aux->next->data.g)){
            a->next = aux->next;
            aux->next = a;
            return SUCCESS;
        }
        aux = aux->next;
    }
    return SUCCESS;
}

int list_find(List *li, Game game){

   if(li == NULL){
        return OUT_OF_MEMORY;
    }
   if(li->head == NULL){
        return 0;
    }
   List_node *aux;
   aux = li->head;
   while(aux->next != NULL){
        if(compara_matriz(aux->data, game)){                        /*funcao compara matriz aqui*/
            return 1;
        }
        else{
            aux = aux->next;
        }

   }
   if(compara_matriz(aux->data, game)){                        /*funcao compara matriz aqui*/
            return 1;
    }
   return 0;
}

int transfer_list(List *origem, List *destino){
    int teste;
   List_node *aux;
   if(origem == NULL){
        return OUT_OF_MEMORY;
    }
    if(destino == NULL){
        return OUT_OF_MEMORY;
    }
   if(origem->head == NULL){
        return INVALID_NULL_POINTER;
    }
    if(destino->head == NULL){
        return INVALID_NULL_POINTER;
    }
   aux = origem->head;
   origem->head = origem->head->next;
   teste = list_insert_sorted(destino, aux->data);
   return teste;
}
