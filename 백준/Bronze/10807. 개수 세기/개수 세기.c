int main()
{
        int N;
        int a[100];
        int i;
        int v;
        int count;
        scanf("%d",&N);
        i = 0;
        while (i < N)
        {
                scanf("%d",&a[i]);
                i++;
        }
        scanf("%d",&v);
        count = 0;
        i = 0;
        while (i < N)
        {
                if (a[i] == v)
                {
                        count++;
                }
                i++;
        }
        printf("%d",count);
}                           