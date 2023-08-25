#include <stdio.h>

int main()
{
        int N;
        scanf("%d",&N);
        int i;
        i = 1;
        while (i<=9)
        {
                printf("%d * %d = %d \n",N,i,N*i);
                i++;
        }
}
