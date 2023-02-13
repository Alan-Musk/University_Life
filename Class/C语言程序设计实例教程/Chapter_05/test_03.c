#include <stdio.h>

int num(double n);
int main(void)
{
    double sum=3.14*3.14/6;
    printf("当n是%d时,最贴近π值.",num(sum));
    return 0;
}
int num(double n)
{
    double sum=0;
    int k=1;
    while(sum<=n)
    {
        sum+=1.0/(k*k);
        k++;
    }
    return k;
}