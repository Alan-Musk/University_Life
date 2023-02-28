// 改错题:给定程序MODI1.C中函数fun的功能是:判断一个整数是否是素数,若是返回1,否则返回0
// 在main()函数中,若fun返回1输出YES,若fun返回0输出NO!
#include <stdio.h>

int fun(int m)
{
    int k=2;
    while(k<=m&&(m%k)!=0)
    {
        k++;
    }
    if(m==k)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main(void)
{
    int n;
    printf("Please enter n:");
    scanf("%d",&n);
    if(fun(n))
    {
        printf("YES!\n");
    }
    else
    {
        printf("NO!\n");
    }
}