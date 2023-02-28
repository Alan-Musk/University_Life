// 改错题:给定程序MODI1.C的功能是:读入一个整数K(2<=k<=10000),打印他的所有质因子(即所有为素数的因子)
// 例如输入整数2310,则因输出2,3,5,7,11
#include <stdio.h>
int IsPrime(int n)
{
    int i,m;
    m=1;
    for(i=2;i<n;i++)
    {
        if(!(n%i))
        {
            m=0;
            break;
        }
    }
    return m;
}
int main(void)
{
    int j,k;
    printf("\nPlease enter an integer number between 2 and 10000:2310");
    scanf("%d",&k);
    printf("\n\nThe prime factor(s) of %d is (are)",k);
    for(j=2;j<=k;j++)
    {
        if((!(k%j))&&(IsPrime(j)))
        {
            printf("\n %4d",j);
        }
    }
    printf("\n");
}