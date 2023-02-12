#include <stdio.h>

int main(void)
{
    int x,y;
    printf("Please input a value of x:");
    scanf("%d",&x);
    if(x<1)
    {
        y=x+1;
    }
    else if(x>=1&&x<10)
    {
        y=2*x+5;
    }
    else if(x>=10)
    {
        y=x*x+8;
    }
    return 0;
}