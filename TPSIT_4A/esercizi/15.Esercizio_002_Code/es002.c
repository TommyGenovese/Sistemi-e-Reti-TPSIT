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

//funzione che controlla se una coda è vuota oppore no
bool is_empty(struct El* head){
    return (head==NULL) ? true: false;
}

//funzione che inserisce un elemento in una coda
void enqueue(struct El** head, struct El** tail, struct El* element){
    if(is_empty(*head)){ 
        *head = element;
    }else{
        (*tail)->next = element;
    }
    *tail = element;
    element->next = NULL;
}

//funzione che toglie il primo elemento di una coda
struct El* dequeue(struct El** head, struct El** tail){
    struct El* ret = *head;

    if(is_empty(*head)) return NULL;
    else *head = ret->next;

    if(*head == NULL) *tail = NULL;

    return ret;
}

int main(){
    struct El* tail = (struct El*) malloc(sizeof(struct El));    //puntatore alla coda
    struct El* head = (struct El*) malloc(sizeof(struct El));    //putatore alla testa
    head = NULL;
    struct El* element; //numero dell'utente
    int numero = 0;
    char risp = 's';  //risposta dell'utente
    int n = 0;  //numero di elementi nella coda

    //continuo a chiedere numeri al'utente fa inserire nella coda
    do{
        system("cls");

        if(is_empty(head)) printf("testa vuota\n");

        //chiedo il numero e lo carico nella struttura
        printf("numero:\t");
        scanf("%d" , &numero);
        printf("\n%p" , head);
        element = (struct El*) malloc(sizeof(struct El));
        element->valore = numero;   

        //inserisco la struttura nella coda
        enqueue(&head, &tail, element);

        //chiedo se vuole inserire altri numeri
        printf("\n%p" , head);
        printf("\n\nAltri numeri? (s/n)  ");
        fflush(stdin);
        scanf("%c" , &risp);

        n++;
    }while(risp == 's' || risp == 'S');

    printf("\nLista:\n");

    //stampo gli elementi nella coda
    for(int i = 0; i<n ; i++){
        printf("%d|" , dequeue(&head,&tail)->valore);
    }
    return 0;
}