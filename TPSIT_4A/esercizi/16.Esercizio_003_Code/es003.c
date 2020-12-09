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



//funzione che inserisce un elemento in una pila
void push(struct El** head, struct El* element){
    if(&head == NULL){
        *head = element;
        element->next = NULL;
    }else{
        element->next = *head;
        *head = element;
    }
}



//funzione che toglie un elemento dalla pila
struct El* pop(struct El** head){
    struct El* ret = *head;
    if(&head == NULL) return NULL;
    else *head = ret->next;
    return ret; 
}





int main(){
    //creo la coda e la testa (inizializzata a NULL)
    struct El* tail = (struct El*) malloc(sizeof(struct El));   //puntatore alla coda
    struct El* head = (struct El*) malloc(sizeof(struct El));   //putatore alla testa
    head = NULL;

    //strutture che contiene il numero 
    struct El* element; //numero dell'utente
    int num = 0; //numero preso da tastiera

    //pila
    struct El* pil;

    char risp = 's';  //risposta dell'utente
    int n = 0;  //numero di elementi nella coda

    //continuo a chiedere numeri al'utente fa inserire nella coda
    do{
        
    }while();

    return 0;
}