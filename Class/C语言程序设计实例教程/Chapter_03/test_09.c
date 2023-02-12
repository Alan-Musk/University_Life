#include <stdio.h>

int main(void)
{
    int number,i,k,m;
    for(int n=100;n<1000;n++)
    {
        i=n%10;         //个位
        k=(n%100-i)/10;      //十位 111
        m=(n-k*10-i)/100;   //百位
        number=m*m*m+k*k*k+i*i*i;
        if(number==n)
        {
            printf("%d\n",number);
        }
    }
    return 0;
}