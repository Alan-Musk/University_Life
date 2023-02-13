#include <stdio.h>

int main(void)
{
    int sum=0;
    for(int n=1;n<101;n++)
    {
        if(n%10==3)
        {
            printf("跳过了%d\n",n);
            continue;
        }
        sum+=n;
    }
    printf("The sum=%d\n",sum);
    return 0;

}