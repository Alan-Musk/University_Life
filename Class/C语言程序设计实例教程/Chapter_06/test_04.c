#include <stdio.h>
#define SIZE 81
int main(void)
{
    char str[SIZE];
    char ch;
    int num=0;
    //输入字符串
    while((ch=getchar())!='\n'&&num<80)
    {
        str[num]=ch;
        num++;
    }
    for(int i=0,j=num-1;i<num/2;i++,j--)
    {
        //将ch作为临时存储
        ch=str[j];
        str[j]=str[i];
        str[i]=ch;
    }
    for(int i=0;i<num;i++)
    {
        printf("%c",str[i]);
    }
    printf("\n");
    return 0;
}