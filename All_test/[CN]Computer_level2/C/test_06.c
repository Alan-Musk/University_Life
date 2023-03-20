// 改错题,给定程序MODI1.c中函数fun的功能是:计算n的5次方的值(规定n的值大于2,小于8),通过形参指针传回主函数
// 并计算该值的个位,十位,百位上的数字之和作为函数值返回
#include <stdio.h>
#include <math.h>
int fun(int n,int *value);
int main(void)
{
    int n,sum,v;
    do
    {
        printf("\nEnter n(2<n<8):   ");
        scanf("%d",&n);
    }while(n<=2||n>=8);
    sum=fun(n,&v);
    printf("\n\nThe result:\n value=%d  sum=%d\n\n",v,sum);
    return 0;
}
int fun(int n,int * value)
{
    int d,s,i;
    d=0;
    s=0;
    d=pow(n,5);
    *value=d;
    for(i=1;i<=3;i++)
    {
        s=s+d%10;
        d=d/10;
    }
    return s;
}