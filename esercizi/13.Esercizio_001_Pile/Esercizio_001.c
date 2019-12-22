/*
Autore: Genovese Tommaso
Data: 19/11/2019
Es 1 pile: crea una pila e la stampa
*/

#include <stdio.h>
#include <stdlib.h>

struct El{        
    int valore;
    float head;
};

int main(){
    struct El* head;
    struct El* element;
    char stringa[1000];
    float num;
    int cifra;
    int i=0;

    do{
        element = (struct El*) malloc(sizeof(struct El));
        element -> valore = stringa[i];
        i++;
        if(head = NULL){
            push(&head, element)
        }else{
            if(head->valore == '{' && element->valore == '}'){
                item = pop(&head);
            }else{
                
            }
            if(head->valore == '[' && element->valore == ']'){
                item = pop(&head);
            }else{

            }
            if(head->valore == '(' && element->valore == ')'){

            }else{
                
            }
        }

    }while()
   
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