#include <stdio.h>
#include <string.h>

int main() {
    int tam = 16; // N�mero de times
    int aux;
    int pontos[] = {16, 8, 15, 15, 21, 14, 5, 0, 2, 9, 7, 5, 10, 12, 13, 14}; 
    int i, j;
    char times[16][64] = {
        "Argentina", "Peru", "Chile", "Canad�",
        "M�xico", "Equador", "Venezuela", "Jamaica",
        "Estados Unidos", "Uruguai", "Panam�", "Bol�via",
        "Brasil", "Col�mbia", "Paraguai", "Costa Rica"
    };
    
    for(i = 0; i < tam; i++) {
        for(j = i + 1; j < tam; j++) {
            if(pontos[j] > pontos[i]) {
                aux = pontos[i];
                pontos[i] = pontos[j];
                pontos[j] = aux;
                
                char temp[64];
                strcpy(temp, times[i]);
                strcpy(times[i], times[j]);
                strcpy(times[j], temp);
            }
        }
    }
    
    for(i = 0; i < tam; i++) {
        printf("Time: %s\n", times[i]);
        printf("Pontos: %i\n\n", pontos[i]);
    }
    
    return 0;
}

