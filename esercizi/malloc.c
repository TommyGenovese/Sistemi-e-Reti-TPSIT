#include <stdlib.h>
#include <stdio.h>

int main(){
    int *punt;
    int num; 
    int n;
    int max;
    int i=0;
    printf("quanti numeri vuoi inserire?");
    scanf("%d", &n);
    punt = malloc(n*sizeof(int));
    while(n>0 && i<n){
        printf("inserisci numero:");
        scanf("%d", &num);
        punt[i]=num;
        i++;
    }
    max = punt[0];
    for(i=1; i<n; i++){
        if(punt[i] > punti[i-1]){
            max = punt[i];
        }
    }
}
