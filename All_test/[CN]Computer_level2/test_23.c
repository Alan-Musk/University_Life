// 填空题: 函数fun功能是把形参a所指的数组中的奇数按原顺序依次存放到a[0],a[1],a[2]..中把偶数从数组中删除
// 奇数个数通过函数值返回,例如,若a所指数组中的数据最初排列为9,1,4,2,3,6,5,8,7.然后为9,1,3,5,7.返回5
#include <stdio.h>
#define N 9
int fun(int a[],int n);
int main(void)
{
    int b[N]={9,1,4,2,3,6,5,8,7},i,n;
    printf("The orginal data:\n");
    for(i=0;i<N;i++)
    {
        printf("%4d ",b[i]);
    }
    printf("\n");
    n=fun(b,N);
    printf("\nThe number of odd:%d\n",n);
    printf("\nThe odd number:\n");
    for(i=0;i<n;i++)
    {
        printf("%4d ",b[i]);
    }
    printf("\n");
    return 0;
}
int fun(int a[],int n)
{
    int num=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]%2==1)
        {
            a[num]=a[i];
            num++;
        }
    }
    return num;
}