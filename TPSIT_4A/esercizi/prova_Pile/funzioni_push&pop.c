//funzioni push & pop delle pile, controllo "if empty"

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
