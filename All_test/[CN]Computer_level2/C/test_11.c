// 填空题:给定程序中,函数fun的功能是将a,b所指的两个字符串分别转换成面值相同的整数
// 并进行相加作为函数值返回,规定字符串只含9个以下的数字字符
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define N 9
long ctod(char * s);
long fun(char * a,char * b);
int main(void)
{
    char s1[N],s2[N];
    printf("Input string s1:");
    fgets(s1,N,stdin);
    printf("Input string s2:");
    fgets(s2,N,stdin);
    printf("The result is:%ld\n",fun(s1,s2));
    return 0;
}
long ctod(char * s)
{
    long d=0;
    while(*s)
    {
        if(isdigit(*s))
        {
            d=d*10+*s-'0';
        }
        s++;
    }
    return d;
}
long fun(char * a,char * b)
{
    return ctod(a)+ctod(b);
}
