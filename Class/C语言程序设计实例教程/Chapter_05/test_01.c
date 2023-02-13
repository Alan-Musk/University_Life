#include <stdio.h>
double func(int x,int y);
int main(void)
{
    int x;
    int n;
    printf("请输入x的值:");
    scanf("%d",&x);
    printf("请输入n的值:");
    scanf("%d",&n);
    printf("值为%.4lf.\n",func(x,n));
    return 0;
}

double func(int x,int n)
{
    double sum=0;
    double up;
    double under;
    for(int j=0;j<=n;j++)
    {
        //上面的分子
        up=1;
        for(int m=1;m<=j;m++)
        {
            up*=x;
        }
        //下面的分母计算
        under=1;
        for(int m=j;m>0;m--)
        {
            under*=m;
        }
        printf("第%d次加:up=%lf,under=%lf.\n",j+1,up,under);
        sum+=up/under;
    }

    return sum;
}