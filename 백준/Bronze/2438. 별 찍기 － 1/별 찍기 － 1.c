#include <stdio.h>

int main()
{
        int N;
        int i;
        int j;
        scanf("%d",&N);
        i=1;
        while (i<=N)
        {
                j=1;
                while (j<=i)
                {
                        printf("*");
                        j++;
                }
                printf("\n");
                i++;
        }
}

