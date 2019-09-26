#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define DELIM ","
#define BSIZE 1024
#define NGAMES 16600    //numero di giochi massimi
#define NAME 30     //numero di caratterri per il nome del gioco
const char SEP = ','; //carattere separatore

//definisco la struttura
    typedef struct game{
        int rank;
        char* name[NAME];
        char* platform[NAME];
        int year;
        char* genre[NAME];
        char* publisher[NAME];
        float NA_Sales;
        float EU_Sales;
        float JP_Sales;
        float Other_Sales;
        float Global_Sales;
    }Game;

//prototipi
void loadTabFromFile(char n[], Game list[]);
void visualizeInfoGame(Game list[]);

int main(){
    //definizione di variabili
    printf("ciao");
    char fileN[NAME] = "vgsales.csv";
    Game list[NGAMES];  //creo la tabella

    //carico la tabella da file
    loadTabFromFile(fileN,list);
    visualizeInfoGame(list);

}


void loadTabFromFile(char n[], Game list[]){
    FILE *fp;
    int k=0;
    char buffer[NAME];

    fp = fopen("vgsales.csv","r");

    if(fp==NULL){
        printf("File %s inesistente\n" , n);
    }else{
        //inizio il ciclo per la copiatura del file in un vettore di strutture
        while(fgets(buffer, BSIZE, fp)){
            if(k==0){
                k=0;   //salto la prima riga
            }else{
                list[k].rank = atoi(strtok(buffer, DELIM));
                list[k].name[NAME] = strtok(NULL, DELIM);
                list[k].platform[NAME] = strtok(NULL, DELIM);
                list[k].year = atoi(strtok(NULL, DELIM));
                list[k].genre[NAME] = strtok(NULL, DELIM);
                list[k].publisher[NAME] = strtok(NULL, DELIM);
                list[k].NA_Sales = atoi(strtok(NULL, DELIM));
                list[k].EU_Sales = atoi(strtok(NULL, DELIM));
                list[k].JP_Sales = atoi(strtok(NULL, DELIM));
                list[k].Other_Sales = atoi(strtok(NULL, DELIM));
                list[k].Global_Sales = atoi(strtok(NULL, DELIM));
                k++;
            }
        }
    }
    fclose(fp);
}

void visualizeInfoGame(Game list[]){
    int n;
    printf("inserisci il numero del gioco");
    scanf("%d", n);
    printf("il nome del giorco è:%s, è per %s, uscito nel %d, di genere %s, dalla %s", list[n].name, list[n].platform, list[n].year, list[n].genre, list[n].publisher);
}