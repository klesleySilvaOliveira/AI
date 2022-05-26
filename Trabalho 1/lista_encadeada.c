#include <stdio.h>
#include <stdlib.h>
#include "lista_encadeada.h"


typedef struct list_node List_node;
typedef struct list List;

struct list{
    List_node *head;
};

struct list_node{
    struct game data;
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

/*int list_print(List *li){
    List_node *a = li->head;
    int i;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    if(li->head == NULL){
        return ELEM_NOT_FOUND;
    }
    while(a != NULL){
        printf("\nMatricula aluno: %d\nNome aluno: %s\nNotas aluno:\n", a->data.matricula, a->data.nome);
        for(i = 0; i < 3; i++){
            printf("- Nota %d: %.2lf\n", i + 1, a->data.n[i]);
        }
        a = a->next;
    }
    return SUCCESS;
}*/

int list_free(List *li){
    List_node *aux, *aux2;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    aux = li->head;
    while(aux != NULL){
        aux2 = aux->next;
        free(aux);
        aux = aux2;
    }
    free(li);
    return SUCCESS;
}

int list_push_front(List *li, struct game game){
    List_node *a;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
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
    List_node *aux;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    if(li->head == NULL){
        return INVALID_NULL_POINTER;
    }
    aux = li->head->next;
    free(li->head);
    li->head = aux;
    return SUCCESS;
}

int list_front(List *li, struct game *game){
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    if(li->head == NULL){
        return INVALID_NULL_POINTER;
    }
    *game = li->head->data;
    return SUCCESS;
}

int list_insert_sorted(List *li, struct game game){
    List_node *aux, *a;
    int back;
    if(li == NULL){
        return OUT_OF_MEMORY;
    }
    back = list_size(li);
    aux = li->head;
    if(back == 0 || game.h < aux->data.h){
        list_push_front(li, game);
        return SUCCESS;
    }

    a = (List_node *)malloc(sizeof(List_node));
    if(a == NULL){
        return OUT_OF_MEMORY;
    }
    a->data = game;

    while(aux != NULL){
        if(game.h > aux->data.h && aux->next == NULL){
            aux->next = a;
            a->next = NULL;
            return SUCCESS;
        }else if(game.h > aux->data.h && game.h < aux->next->data.h){
            a->next = aux->next;
            aux->next = a;
            return SUCCESS;
        }
        aux = aux->next;
    }
    return SUCCESS;
}
