// 改错题:已知一个数列从第0项开始的前三项分别是0,0,1,以后的各项都是其相邻的前三项之和,给定程序MODI1.C中函数fun的功能是:计算并输出该数列前n项的平方根之和,n的值通过形参传入
#include <stdio.h>
#include <math.h>

float fun(int n)
{
    double sum=1.0,s0,s1,s2,s;
    int k;
    if(n<=2)
    {
        sum=0.0;
    }
    s0=0.0;s1=0.0;s2=1.0;
    for(k=4;k<=n;k++)
    {
        s=s0+s1+s2;
        sum+=sqrt(s);
        s0=s1;
        s1=s2;
        s2=s;
    }
    return sum;
}
int main(void)
{
    int n;
    printf("Input N=");
    scanf("%d",&n);
    printf("%f\n",fun(n));
    return 0;
}