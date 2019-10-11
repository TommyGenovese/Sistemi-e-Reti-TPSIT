#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define DELIM ","
#define BSIZE 1024
#define NGAMES 16600    //numero di giochi massimi
#define NAME 30     //numero di caratterri per il nome del gioco
const char SEP = ','; //carattere separatore

//definisco la strutturaww
    typedef struct game{
        int rank;
        char* name;
        char* platform;
        int year;
        char* genre;
        char* publisher;
        float NA_Sales;
        float EU_Sales;
        float JP_Sales;
        float Other_Sales;
        float Global_Sales;
    }Game;

//prototipi
void loadTabFromFile(char n[], Game list[]);
void visualizeInfoGame(Game list[], int n);

int main(){
    //definizione di variabili

    int n, l;
    char fileN[NAME] = "vgsales.csv";
    char answer;
    Game list[NGAMES];  //creo la tabella


    //carico la tabella da file
    
    printf("inizio");

    loadTabFromFile(fileN,list);
    n=NGAMES;
    printf("Do you wanna know which is the most popular game in America?\n");
    scanf("%c", &answer);
    if(answer=='s' || answer=='S'){
      visualizeInfoGame(list, n);
    }


}


void loadTabFromFile(char n[], Game list[]){
    FILE *fp;
    int k=0;
    char primaR[NGAMES];
    char buffer[NAME];

    fp = fopen("vgsales.csv","r");

    if(fp==NULL){
        printf("File %s inesistente\n" , n);
    }else{
        //inizio il ciclo per la copiatura del file in un vettore di strutture
        fgets(primaR, BSIZE, fp); 
        while(fgets(buffer, BSIZE, fp)){
            list[k].rank = atoi(strtok(buffer, DELIM));
            list[k].name = strtok(NULL, DELIM);
            list[k].platform = strtok(NULL, DELIM);
            list[k].year = atoi(strtok(NULL, DELIM));
            list[k].genre = strtok(NULL, DELIM);
            list[k].publisher = strtok(NULL, DELIM);
            list[k].NA_Sales = atof(strtok(NULL, DELIM));
            list[k].EU_Sales = atof(strtok(NULL, DELIM));
            list[k].JP_Sales = atof(strtok(NULL, DELIM));
            list[k].Other_Sales = atof(strtok(NULL, DELIM));
            list[k].Global_Sales = atof(strtok(NULL, DELIM));
            k++;
        }
        printf("\nHo letto il file\n");
    }
    fclose(fp);
}

void visualizeInfoGame(Game list[], int n){
    printf("visualizeINfoGame");
    int k;
    int cont=0;
    float max=0;
    for(k=0; k<n; k++){
      if(list[k].NA_Sales > max){
        max=list[k].NA_Sales;
        cont=k;
      }
    }
    printf("\nThe most popular game in America is %s\n\n", list[cont].name);

}
