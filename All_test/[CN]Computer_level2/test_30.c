// 改错题:给定程序MODI1.C中函数fun的功能是:在字符串的最前端加入n个*号,形成新串,并覆盖原串,最长为79
#include <stdio.h>
#include <string.h>

void fun(char s[],int n)
{
    char a[80],*p;
    int i;
    p=s;
    for(i=0;i<n;i++)
    {
        a[i]='*';
    }
    do
    {
        a[i]=*p;
        i++;
    }while(*p++);
    a[i]=0;
    strcpy(s,a);
}
int main(void)
{
    int n;
    char s[80];
    printf("\nEnter a string : ");
    fgets(s,80,stdin);
    printf("\nThe string \"%s\"\n",s);
    printf("\nEnter n(number of *):");
    scanf("%d",&n);
    fun(s,n);
    printf("\nThe string after insert:\"%s\"",s);
    return 0;
}