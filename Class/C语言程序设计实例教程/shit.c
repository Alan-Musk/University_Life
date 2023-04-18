#include <stdio.h>

int main(void)
{
    char ch;
    char chs[101]; //申明数组
    int total=0;//字符串字符总和
    int yes=1;//初始假定是回文串
    //获取字符串
    while((ch=getchar())!='\n')
    {
        chs[total]=ch;
        total++;
    }
    // 开始判断
    for(int i=0,j=total-1;i<j;i++,j--)
    {
        if(chs[i]!=chs[j])
        {
            yes=0;
            break;
        }
    }
    if (yes==1)
    {
        printf("是回文");
    }
    else
    {
        printf("不是回文");
    }
    return 0;

}