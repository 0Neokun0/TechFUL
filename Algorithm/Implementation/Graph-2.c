#include <stdio.h>

int main()
{
    int N, i, j;

    // printf("Enter N:\n");
    scanf("%d", &N);

    for(i=1; i<=N+1; i++)
    {
        // Print first part
        for(j=i; j>1; j--)
        {
            printf("*");
        }

        // Print second part
        for(j=1; j<= (N-i)+1; j++)
        {
            printf("-");
        }

        printf("\n");
    }

    return 0;
}