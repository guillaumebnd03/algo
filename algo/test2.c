#include <stdio.h>
#include <stdlib.h>


int main() {
    int rows, cols;

    printf("Entrez le nombre de lignes: ");
    scanf("%d", &rows);

    printf("Entrez le nombre de colonnes: ");
    scanf("%d", &cols);

    int **tableau = (int **) malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        tableau[i] = (int *) malloc(cols * sizeof(int));
    }

    FILE *fichier = fopen("sudoku.txt", "r");
    if (fichier == NULL) {
        printf("Impossible d'ouvrir le fichier\n");
        exit(1);
    }

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            fscanf(fichier, "%d", &tableau[i][j]);
        }
    }

    fclose(fichier);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            tableau[i][j] = i * j;
        }
    }

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", tableau[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < rows; i++) {
        free(tableau[i]);
    }
    free(tableau);

    return 0;
}