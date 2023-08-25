#include <stdio.h>

int main()
{
        int N;
        int a[1000000];
        int i;
        int max;
        int min;

        scanf("%d",&N);
        i = 0;
        while (i < N)
        {
                scanf("%d",&a[i]);
                i++;
        }
        i = 0;
        max = a[0];
        min = a[0];
        while (i < N)
        {
                if (max < a[i])
                {
                        max = a[i];
                }
                if (min > a[i])
                {
                        min = a[i];
                }
                i++;
        }
        printf("%d %d",min,max);
}
