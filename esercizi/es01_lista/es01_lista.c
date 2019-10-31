/*crea una lista e la stampa*/
#include <stdio.h>
#include <stdlib.h>
struct El
{
    int valore;
    struct El *next; 
};
int main()
{
    int n;
    struct El *lista;
    struct El *l;
    lista = NULL; // il puntatore non punta a niente
    do
    {
        printf("Inserisci un naturale o -1 per terminare\n");
        scanf("%d", &n);
        if (n >= 0)
        {
            if (lista == NULL) //se lista punta a NULL riservo lo spazio di un nuovo elemento della lista e assegno l
            {
                /*  */
                lista = (struct El *)malloc(sizeof(struct El));
                l = lista;
            }
            else /* COMMENTO */
            {
                /* COMMENTO */
                l->next = (struct El *)malloc(sizeof(struct El));
                l = l->next;
            }
            l->valore = n;  /* COMMENTO */
            l->next = NULL; /* COMMENTO */
        }
    } while (n >= 0);
    l = lista; /* COMMENTO */
    printf("numeri inseriti: \n");
    while (l != NULL)
    {
        printf("%d - %p \n", l->valore, l->next);
        l = l->next; /* COMMENTO */
    }
    printf("\n");
    return 0;
}