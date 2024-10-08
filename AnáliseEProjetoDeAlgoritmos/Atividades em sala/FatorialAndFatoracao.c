#include <stdio.h>


int fatorial(int x) {
	int i;
	for(i = x - 1; i >0; i--) {
		x = x * i;
	}
	return x;
}

void fatorar(int n) {
	int i;
    printf("Fatores de %i: ", n);
    for (i = 2; i <= n; i++) {
        while (n % i == 0) {
            printf("%i ", i);
            n /= i;
        }
    }
    printf("\n");
}


int main() {
	int n, opcao = 0, result;
	
	do {
		printf("Digite 1 para ver o fatorial e 0 para fatoracao: ");
		scanf("%i", &opcao);
	}while( !(opcao == 0  || opcao == 1));
	    printf("Informe o número: ");
	    scanf("%i", &n);
	    if(opcao == 1) {
	    
	    	result =fatorial(n);
	    	printf("%i", result);
	    	
		}else {
			fatorar(n);
		}
	  
}
