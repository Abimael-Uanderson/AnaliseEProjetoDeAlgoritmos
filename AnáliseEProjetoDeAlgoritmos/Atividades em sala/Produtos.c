#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura que representa um produto
typedef struct produto {
    char nome[50];
    int id;
} Produto;

// Função para exibir as informações de um produto
void exibirProduto(Produto *p) {
    printf("\n\nNome do produto: %s\n", p->nome);
    printf("ID do produto: %d\n", p->id);
}

// Função para exibir todos os produtos em um vetor
void exibirProdutos(Produto *produtos, int total) {
	int i;
    for (i = 0; i < total; i++) {
        exibirProduto(&produtos[i]);
    }
}

// Função para ordenar produtos pelo nome
void ordenarPorNome(Produto *produtos, int total) {
    Produto temp;
    int i, j;
    for (i = 0; i < total - 1; i++) {
        for (j = i + 1; j < total; j++) {
            if (strcmp(produtos[i].nome, produtos[j].nome) > 0) {
                temp = produtos[i];
                produtos[i] = produtos[j];
                produtos[j] = temp;
            }
        }
    }
}

// Função para buscar um produto pelo ID usando busca binária
int buscarPorID(Produto *produtos, int total, int id) {
    int inicio = 0;
    int fim = total - 1;

    while (inicio <= fim) {
        int meio = (inicio + fim) / 2;
        if (produtos[meio].id == id) {
            return meio;
        } else if (produtos[meio].id < id) {
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return -1;
}

// Função para adicionar um novo produto ao vetor
void adicionarProduto(Produto *produtos, int *total) {
    printf("\n\nDigite o ID do produto: ");
    scanf("%d", &produtos[*total].id);

    printf("Digite o nome do produto: ");
    scanf("%s", produtos[*total].nome);

    (*total)++;
}

int main(void) {
    Produto produtos[10];
    int totalProdutos = 0;
    int opcao;

    do {
        printf("\n=============================\n");
        printf("         Menu Principal       \n");
        printf("=============================\n");
        printf("1. Adicionar Novo Produto\n");
        printf("2. Buscar Produto Específico\n");
        printf("3. Ordenar Produtos pelo Nome\n");
        printf("4. Listar Todos os Produtos\n");
        printf("0. Sair do Sistema\n");
        printf("=============================\n");
        printf("Selecione uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                adicionarProduto(produtos, &totalProdutos);
                break;
            case 2: {
                int id;
                printf("\nDigite o ID do produto que deseja buscar: ");
                scanf("%d", &id);
                int posicao = buscarPorID(produtos, totalProdutos, id);
                if (posicao != -1) {
                    printf("\nProduto encontrado na posição %d: \n", posicao);
                    exibirProduto(&produtos[posicao]);
                } else {
                    printf("\nProduto não encontrado!");
                }
                break;
            }
            case 3:
                ordenarPorNome(produtos, totalProdutos);
                printf("\nProdutos ordenados com sucesso!\n");
                break;
            case 4:
                exibirProdutos(produtos, totalProdutos);
                break;
            case 0:
                printf("\nFim\n");
                break;
            default:
                printf("\nOpção inválida");
        }

    } while (opcao != 0);
    return 0;
}

