#include <stdio.h>

int main(void)
{
    int num1=1,num2=1,num3;
    printf("%d %d ",num1,num2);
    for(int n=3;n<41;n++)
    {
        num3=num1+num2;
        printf("%d ",num3);
        num1=num2;
        num2=num3;
    }
    return 0;
}