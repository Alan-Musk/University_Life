#include <stdio.h>
#include <math.h>
double fun(double x,int n);
int main(void)
{
    printf("%f\n",fun(0.3,10));
    return 0;
}

double fun(double x,int n)
{
    double sum=1.0;
    double temp=1;
    for(int i=1;i<=n;i++)
    {
        temp*=x/i;
        sum+=temp;
    }
    return sum;
}