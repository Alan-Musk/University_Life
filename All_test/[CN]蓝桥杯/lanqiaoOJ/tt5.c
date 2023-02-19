// 门牌从 0 到 2020
#include <stdio.h>

int main(void)
{
    int sum=0;

    for(int i=1;i<=2020;i++)
    {
        for(int j=i;j>=1;j/=10)
        {
            if(j%10==2)
            {
                sum++;
            }
        }
    }
    printf("%d",sum);
}