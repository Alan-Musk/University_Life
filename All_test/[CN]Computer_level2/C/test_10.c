// 函数fun的功能是把两个两位数的正整数a,b合并形成一个整数放在c中,合并的方式是将a数的十位和个位数依次放在c数的个位和百位上,b数的十位和个位数依次放在C数的千位和十位上
#include <stdio.h>
void fun(int a,int b,long * c);

int main(void)
{
    int a,b;
    long c;
    printf("Input a b:");
    scanf("%d %d",&a,&b);
    fun(a,b,&c);
    printf("The result is:%ld\n",c);
    return 0;
}
void fun(int a,int b,long * c)
{
    *c=a%10*100+a/10%10+b%10*10+b/10%10*1000;
}