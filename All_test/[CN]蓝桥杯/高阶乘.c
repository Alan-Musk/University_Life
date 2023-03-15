//输入一个正整数n,输出n!的值,n<=1000
#include <stdio.h>
#define N 10000
int a[N]={0};
int main(void)
{
    int n;
    intw carry;
    scanf("%d",&n);
    a[0]=1;
    for(long long i=1;i<=n;i++)
    {
        carry=0;
        for(long long j=0;j<N;j++)
        {
            a[j]=a[j]*i+carry;
            carry=a[j]/10;
            a[j]=a[j]%10;
        }
    }
    int count=0;
    for(int i=N-1;i>=0;i--)
    {
        if(a[i]!=0)
        {
            count=i;
            break;
        }
    }
    for(;count>=0;count--)
    {
        printf("%d",a[count]);
    }
    printf("\n");
    return 0;
}