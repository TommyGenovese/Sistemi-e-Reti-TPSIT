//visualizzare un albero e inserire un elemento
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

/* definizione di albero */
typedef struct nodo {
  	double radice;
  	struct nodo *sx;
	struct nodo *dx;
}NODO;
typedef struct NODO *Albero;

Albero costruisci(Albero,int);
void StampaAlbero(Albero);

/*void insert(struct tree_node **tree, struct tree_nodes *new)
{
	if (*tree == NULL)
	{
		*tree = new;
		(*tree)->left = NULL;
		(*tree)->right = NULL;
	}
	else
	{
		if (new->key < (*tree)->key)
		{
			Insert(&(*tree)->left, new);
		}
		else if (new->key > (*tree)->key)
		{
			Insert(&(*tree)->right, new);
		}
		else
			printf("Chiave duplicata\n");
	}
}*/

Albero costruisci(Albero a,int n){
        srand(time(NULL));
        int i;
        if(n==0)
          a=NULL;
        else{
          for(i=1;i<=n;i++)     
          a=(NODO*)malloc(sizeof(NODO));
          (*a)->radice=(rand()%20)-20;
          a->sx->radice=(a->sx,i);
          a->dx->radice=(a->dx,i);
          }
        return a;
} 

// stampa in ordine dell'albero a
void StampaAlbero(Albero a) {
  if(a==NULL) {
    printf("()");
    return;
  }

  printf("( %d ", a->radice);
  StampaAlbero(a->sx);
  StampaAlbero(a->dx);
  printf(" ) ");
}

int main(){
    Albero a;
    int n,i;
    printf("Quanti elementi devono essere inseriti?\n");
    scanf("%d",&n);
    a=costruisci(a,n);
    StampaAlbero(a);
    // system("pause");
}