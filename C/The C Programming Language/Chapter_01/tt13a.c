// 实现直方图,水平方向
#include <stdio.h>
#define SIZE 10
int main(void)
{
    int ch;
    int words[SIZE];
    int i=0;
    //计入数组
    while((ch=getchar())!=EOF&&i<10)
    {
        if(ch=='\n'||ch==' '||ch=='\t'||ch=='.'||ch==',')
        {
            i++;
        }
        else
        {
            words[i]++;
        }
    }
    //输出
    i=0;
    for(i=0;i<SIZE&&words[i]!=0;i++)
    {
        for(int j=words[i];j>0;j--)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}