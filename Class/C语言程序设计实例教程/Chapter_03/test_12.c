#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    bool prime;
    for(int n=100;n<=200;n++)
    {
        prime=true;
        int temp=0;
        for(int j=2;j*j<=n;j++)
        {
            if(n%j==0)
            {
                prime=false;
                break;
            }
        }
        if(prime)
        {
            printf("%d是素数.\n",n);
        }
    }
    return 0;
}