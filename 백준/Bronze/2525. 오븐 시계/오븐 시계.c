#include <stdio.h>

int main()
{
        int A;
        int B;
        int C;
        int D;
        int E;
        scanf("%d %d\n%d",&A,&B,&C);
        D=C/60;
        E=C%60;

        if(B+E>=60)
        {
                if(A+D+1>=24)
                {
                        printf("%d %d",A+D+1-24,B+E-60);
                }
                else
                {
                        printf("%d %d",A+D+1,B+E-60);
                }
        }
        else
        {
                if(A+D>=24)
                {
                        printf("%d %d",A+D-24,B+E);
                }
                else
                {
                        printf("%d %d",A+D,B+E);
                }
        }
}