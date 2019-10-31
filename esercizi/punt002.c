#include <stdlib.h>
#include <stdio.h>

int main(){
    float* v;
    int dim, k;

    printf("insersci la dimesione del vettore: ");
    scanf("\n%d\n", &dim);

    v = (float*)malloc(dim * sizeof(float));

    for(k=0; k<dim; k++){
        scanf("%f", v+k);
    }

}