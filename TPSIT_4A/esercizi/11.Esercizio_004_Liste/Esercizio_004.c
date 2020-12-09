/*
Autore: Genovese Tommaso
Data: 12/11/2019
Es 4 liste: Definire una funzione deallocaLista che riceve una ListaDiElementi e ne dealloca tutti gli elementi. 
*/
#include <stdio.h>
#include <stdlib.h>

struct El{
    int valore;
    struct El* next;
};

void stampaLista(struct El* l);
void liberaMemoria(struct El* l);


int main(int argc, char const *argv[]){
    /* code */
    int n;
    struct El* lista;   //puntatore al primo elemento
    struct El* l;
    lista = NULL;   //inizializzo il puntatore a null

    do{
        /* code */
        printf("Inserisci un naturale o -1 per terminare\n");
        scanf("%d", &n);
        if (n>=0){
            /* code */
            if (lista == NULL){
                /* code */
                lista = (struct El*) malloc(sizeof(struct El));
                l = lista;
            }else{
                /* code */
                //assegnoal puntatore l dell'elemento corrente un puntatore che punta all'elemento successivo
                l->next = (struct El*) malloc(sizeof(struct El));
                l =  l->next;
            }
            l->valore = n;  //assegno n al campo valore dell'elemento corrente
            l->next = NULL; //assegno al campo next dell'elemento correnteil valore NULL
        }
    } while (n>=0);

    stampaLista(lista);
    liberaMemoria(lista); 
    printf("\n\n");
    return 0;
}

void stampaLista(struct El* l){
    if (l->next != NULL){
        /* code */
        printf("%d - %p \n",l->valore, l->next);
        stampaLista(l->next);
    }else{
        /* code */
        printf("%d - %p \n",l->valore, l->next);
    }
}

void liberaMemoria(struct El* l){
    if (l->next != NULL){
        /* code */
        liberaMemoria(l->next);
    }
    free(l);
    printf("Free\n");
}