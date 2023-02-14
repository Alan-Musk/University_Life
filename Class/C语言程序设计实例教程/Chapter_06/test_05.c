#include <stdio.h>
#include <ctype.h>
#define SIZE 81
int main(void)
{
    char str[SIZE];
    int num=0,sum=0;
    char ch;
    while((ch=getchar())!='\n'&&num<80)
    {
        str[num]=ch;
        num++;
    }
    for(int i=0;i<num;i++)
    {
        if(isalpha(str[i]))
        {
            sum++;
        }
    }
    printf("字母的个数是%d,非字母的个数是:%d.\n",sum,num-sum);
    return 0;
}