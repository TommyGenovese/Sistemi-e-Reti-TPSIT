/*
Autore: Genovese Tommaso
Data: 19/11/2019
Es 1 pile: crea una lista e la stampa
*/

#include <stdio.h>
#include <stdlib.h>

struct El{        
    int valore;
    float head;
};

int main(){
    float num;
    int cifra;
    char element;
    
   printf("inserisci il numero: ");
   scanf("%d\n", &cifra);
   *element = cifra;
   push(*head, *element);
   
}

 void push(struct stack_node **head, struct stack_node *element){
    if(is_empty(*head)){
        *head = element;
        element->next= NULL;
    }else{
        element->next = *head;
        *head = element; 
    }
}

struct stack_node *pop(struct stack_node **head){
    struct stack_node *ret = *head;

    if(is_empty(*head)){
        printf("error: empty stack");
        return NULL;
    }else{
        *head = ret->next;
    }
    return ret;
}