#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TIPO 2


//funzione che inserisce un elemento in una pila
void push(struct El** head, struct El* elements[]){
    if(&head == NULL){
        *head = elements[];
        elements[]->next = NULL;
    }else{
        elements[]->next = *head;
        *head = elements[];
    }
}

//funzione che toglie un elemento dalla pila
struct El* pop(struct El** head){
    struct El* ret = *head;
    if(&head == NULL) return NULL;
    else *head = ret->next;
    return ret; 
}

//creazione della struttura auto-referenziata
struct El{
    char segno;
    int num;
    struct El* next;

}El;

main(){
    struct El* head;
    struct El* elements[TIPO];
    struct El* ret;

    //creo le carte con un for (per il segno) con dentro altri for (per i numeri)
    for(c=0; c<52; c++){
        elements[] = (struct El*) malloc(sizeof(struct El)*2);
        if(c>12){
            if(c>26){
                if(c>40){
                    elemsegno[1] -> segno = 'F';
                    for(int n=0; n<13; n++){
                        element[0] -> num = n+1;
                        push(&head, elements[]);
                        printf("la carta e' di segno: %c e vale %d", elements[1], elements[0]); //stampa il valore della carta
                    }
                }else{
                    elemsegno[1] -> segno = 'D';
                    for(int n=0; n<13; n++){
                        element[0] -> num = n+1;
                        push(&head, elements[]);
                        printf("la carta e' di segno: %c e vale %d", elements[1], elements[0]); //stampa il valore della carta
                    }
                }
            }else{
                elemsegno[1] -> segno = 'P';
                for(int n=0; n<13; n++){
                    element[0] -> num = n+1;
                    push(&head, elements[]);
                    printf("la carta e' di segno: %c e vale %d", elements[1], elements[0]); //stampa il valore della carta
                }
            }
        }else{
            elemsegno[1] -> segno = 'C';
            for(int n=0; n<13; n++){
                element[0] -> num = n+1;
                push(&head, elements[]);
                printf("la carta e' di segno: %c e vale %d", elements[1], elements[0]); //stampa il valore della carta
            }
        }
    }

    mescola_mazzo(elements[]);
}


//questa funzione mescola il mazzo
void mescola_mazzo(int p[])
{
  int s, c;
  /* */
  for(s=0; s<51; s++)
    p[s] = s;
  /* Inizializziamo il seme della successione di numeri casuali
     utilizzando la function time */
  srand( time(0) );

  /* Effettuiamo un ciclo su s che corre da 0 a 51 */
  for(s=0; s<52; s++) {
    c = floor( (rand() * 52.) / (RAND_MAX + 1.) );
    int tmp;
    tmp = p[s];
    p[s] = p[c];
    p[c] = tmp;
  }

}