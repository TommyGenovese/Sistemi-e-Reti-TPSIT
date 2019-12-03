/*
   Authors: Bruno Luca & Genovese Tommaso 
  
   ES1:Implementare i metodi enqueue() e dequeue() e creare un programma che permetta all’utente di
       riempire una coda di numeri interi di lunghezza arbitraria. Successivamente testare la funzione
       dequeue per svuotare la coda.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct El{
    int valore;
    struct El* next;
}El;

//funzione che inserisce un elemento in una coda
void enqueue(struct El** head, struct El** tail, struct El* element){
    if(&head == NULL){ 
        printf("primo if\n");
        *head = element;
    }else{
        (*tail)->next = element;
        printf("primo else\n");
    }
    printf("finito controllo\n");
    *tail = element;
    element->next = NULL;
}

//funzione che toglie il primo elemento di una coda
struct El* dequeue(struct El** head, struct El** tail){
    struct El* ret = *head;

    if(&head == NULL) return NULL;
    else *head = ret->next;

    if(*head == NULL) *tail = NULL;

    return ret;
}

int main(){
    struct El* tail = (struct El*) malloc(sizeof(struct El));    //puntatore alla coda
    struct El* head = NULL;    //putatore alla testa
    struct El* element; //numero dell'utente
    int numero = 0;
    char risp = 's';  //risposta dell'utente

    //continuo a chiedere numeri al'utente fa inserire nella coda
    do{
        system("cls");

        //carico il numero nella struttura
        printf("numero:\t");
        scanf("%d" , &numero);
        //printf("numero = %d" , numero);
        printf("%p" , &head);
        element = (struct El*) malloc(sizeof(struct El));
        element->valore = numero;   

        //inserisco la struttura nella coda
        enqueue(&head, &tail, element);

        //cheido vuole inserire altri numeri
        printf("%p" , head);
        printf("\n\nAltri numeri? (s/n)  ");
        fflush(stdin);
        scanf("%c" , &risp);
    }while(risp == 's' && risp == 'S');

    printf("|CARICAMENTO COMPLETATO|");
    return 0;
}