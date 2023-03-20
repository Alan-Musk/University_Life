// 改错题:给定程序MODI1.C中函数fun的功能是,求出两个非零正整数的最大公约数,并作为函数值返回
// 比如49,21,则最大公约数是7
#include <stdio.h>
int fun(int a,int b)
{
    int r,t;
    if(a<b)
    {
        t=a;
        b=a;
        b=t;
    }
    r=a%b;
    while(r!=0)
    {
        a=b;
        b=r;
        r=a%b;
    }
    return b;
}
int main(void)
{
    int num1,num2,a;
    printf("Input num1 num2:   ");
    scanf("%d %d",&num1,&num2);
    printf("num1=%d num2=%d\n\n",num1,num2);
    a=fun(num1,num2);
    printf("The maximum common divisor is %d\n\n",a);
    return 0;
}