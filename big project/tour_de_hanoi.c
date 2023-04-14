#include <stdio.h>

void hanoi(int n, char A, char B, char C)
{
    if (n == 1)
    {
        printf("Deplacez le disque 1 de %c vers %c\n", A, C);
        return;
    }
    hanoi(n-1, A, C, B);
    printf("Deplacez le disque %d de %c vers %c\n", n, A, C);
    hanoi(n-1, B, A, C);
}

int main()
{
    int n = 3;
    hanoi(n, 'A', 'B', 'C');
    return 0;
}