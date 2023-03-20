#include <stdio.h>
#include <math.h>
double fun(double x);
int main(void)
{
    double x,y;
    x=2.5;
    y=fun(x);
    printf("\nThe result is:\n");
    printf("x=%-12.6f   y=%-12.6f\n",x,y);
    return 0;
}
double fun(double x)
{
    double f,t;
    int n;
    f=1.0+x;
    t=x;
    n=1;
    do
    {
        n++;
        t*=x/n;
        f+=t;
    }while(fabs(t)>=1e-6);
    return f;
}