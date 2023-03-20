// 请编写一个函数fun,它的功能是:求出1到m之间(含m)能被7或11整除的所有整数,放在数组a中,通过n返回这些数的个数.
// 例如 m=50,则输出:7 11 14 21 22 28 33 35 42 44 49
#include <stdio.h>
#define M 50
void fun(int m,int *a,int *n);
int main(void)
{
    int aa[M],n,k;
    fun(50,aa,&n);
    for(k=0;k<n;k++)
    {
        if((k+1)%20==0)
        {
            printf("\n");
        }
        else
        {
            printf("%4d",aa[k]);
        }
    }
    printf("\n");
    return 0;
}
void fun(int m,int *a,int *n)
{
    for(int i=7;i<=m;i++)
    {
        if((i%11==0) ||(i%7)==0)
        {
            *n+=1;
            *a=i;
            a++;
        }
    }
}