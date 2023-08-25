#include <stdio.h>

int main()
{
        int T;
        int A;
        int B;
        int i;

        scanf("%d",&T);

        i=0;
        while (i<T)
        {
                scanf("%d %d",&A,&B);
                printf("Case #%d: %d\n",i+1,A+B);
                i++;
        }
}
