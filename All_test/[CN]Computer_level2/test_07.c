// 编程题:请编写函数fun,其功能是:计算并输出给定数组(长度为9)中每相邻两个元素之平均值的平方根的和
#include <stdio.h>
#include <math.h>

double fun(double x[9]);
int main(void)
{
    double s,a[9]={12.0,34.0,4.0,23.0,34.0,45.0,18.0,3.0,11.0};
    int i;
    printf("The original data is :\n");
    for(i=0;i<9;i++)
    {
        printf("%6.1f",a[i]);
    }
    printf("\n\n");
    s=fun(a);
    printf("s=%f\n\n",s);
    return 0;
}
double fun(double x[9])
{
    double sum=0;
    for(int i=1;i<9;i++)
    {
        sum+=sqrt((x[i-1]+x[i])/2);
    }
    return sum;
}