#include <stdio.h>

int main(void)
{
    float price1,price2,price3;
    float sum;
    printf("Please input the prices of three goods.");
    scanf("%f %f %f",&price1,&price2,&price3);
    sum=price1+price2+price3;
    if(price1>50||price2>50||price3>50||sum>100)
    {
        sum*=0.85;
    }
    printf("您应该付%f.\n",sum);
    return 0;
}