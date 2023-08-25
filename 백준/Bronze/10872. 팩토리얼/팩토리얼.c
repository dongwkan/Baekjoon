#include <stdio.h>

int facto(int x)
{
        if (x == 0)
        {
                return 1;
        }
        else
        {
                return x * facto(x-1);
        }
}

int main()
{
        int N;
        int R;
        scanf("%d",&N);
        R = facto(N);
        printf("%d",R);
}
