// 编程题:假定输入的字符串中只含有字母和*号.请编写函数fun,它的功能是:删除字符串中所有的*号.在编写函数时,不能使用C语言提供的字符串函数
#include <stdio.h>
void fun(char * a);
int main(void)
{
    char s[81];
    printf("Enter a string:\n");
    fgets(s,81,stdin);
    fun(s);
    printf("The string after deleted:\n");
    fputs(s,stdout);
    return 0;
}
void fun(char * a)
{
    int i=0,j=0;
    while(a[i])
    {
        if(a[i]!='*')
        {
            a[j++]=a[i];
        }
        i++;
    }
    a[j]=0;
}