#include <stdlib.h>
#include <stdio.h>


void insert(struct tree_node **tree, struct tree_nodes* new){
	if(*tree == NULL){
		*tree= new;
        (*tree)-> left = NULL;
		(*tree)->right = NULL;
	}else{
		if(new->key < (*tree)->key){
			Insert(&(*tree)->left, new);
		}else if(new->key > (*tree)->key){
			Insert(&(*tree)->right, new);
		}else
			Printf("Chiave duplicata\n");
	}
}