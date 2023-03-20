// 改错题:假定整数数列中的数不重复,并存放在数组中.给定程序MODI1.c中函数fun的功能是:删除数列中值为x的元素,n中存放的是数列中元素的个数
#include <stdio.h>
#define N 20
int fun(int * a,int n,int x);
int main(void)
{
    int w[N]={-3,0,1,5,7,99,10,15,30,90};
    int x,n,i;
    n=10;
    printf("The original data:\n");
    for(i=0;i<n;i++)
    {
        printf("%5d",w[i]);
    }
    printf("\nInput x(to delete):");
    scanf("%d",&x);
    n=fun(w,n,x);
    if(n==-1)
    {
        printf("***Not be fund!***\n\n");
    }
    else
    {
        printf("The data after deleted:\n");
        for(i=0;i<n;i++)
        {
            printf("%5d",w[i]);
        }
        printf("\n\n");
    }
}
int fun(int * a,int n,int x)
{
    int p=0;
    int i;
    while(x!=a[p])
    {
        p+=1;
    }
    if(p==n)
    {
        return -1;
    }
    else
    {
        for(i=p;i<n-1;i++)
        {
            a[i]=a[i+1];
        }
        return n-1;
    }
}