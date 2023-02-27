// 改错题:给定程序MODI1.C中fun函数的功能是:分别统计字符串大写字母和小写字母的个数
#include <stdio.h>

void fun(char * s,int * a,int * b);
int main(void)
{
    char s[100];
    int upper=0;
    int lower=0;
    printf("\nPlease a string:  ");
    fgets(s,100,stdin);
    fun(s,&upper,&lower);
    printf("\nupper=%d lower=%d\n",upper,lower);
    return 0;
}

void fun(char * s,int * a,int * b)
{
    while(*s)
    {
        if(*s>='A'&&*s<='Z')
        {
            *a+=1;
        }
        else if(*s>='a'&&*s<='z')
        {
            *b+=1;
        }
        s++;
    }
}