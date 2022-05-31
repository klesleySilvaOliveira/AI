#define SUCCESS 0
#define INVALID_NULL_POINTER -1
#define OUT_OF_MEMORY -2
#define OUT_OF_RANGE -3
#define ELEM_NOT_FOUND -4

struct game{
    int matriz[3][3], g, h;
};

typedef struct list List;
typedef struct game Game;

List* list_create();
int list_free(List *li);
int list_insert_sorted(List *li, Game game);
int list_size(List *li);
int list_pop_front(List *li);
int list_front(List *li, Game *game);
int list_find(List *li, Game game);
int transfer_list(List *origem, List *destino);
