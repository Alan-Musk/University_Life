// 给定程序MODI1.C中函数fun的功能是:用选择法对数组中的n个元素从小到大的顺序进行排序
#include <stdio.h>
#define N 20
void fun(int a[],int n);
int main(void)
{
    int a[N]={9,6,8,3,-1},i,m=5;
    printf("排序之前的数据:");
    for(i=0;i<m;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    fun(a,m);
    printf("排序之后的数据:");
    for(i=0;i<m;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    return 0;
}
void fun(int a[],int n)
{
    int i,j,t,p;
    for(j=0;j<n-1;j++)
    {
        p=j;
        for(i=j+1;i<n;i++)
        {
            if(a[i]<a[p])
            {
                p=i;
            }
            t=a[p];
            a[p]=a[j];
            a[j]=t;
        }
    }
}