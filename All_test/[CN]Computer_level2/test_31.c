// 编程题:请编写函数fun,功能是:统计各年龄段的人数.N个年龄通过调用随机函数获得,并放在主函数的age数组中;
// 要求函数把0-9岁年龄段的人数放在d[0],把10-19岁放在d[1]中一次类推,把100岁以上放在d[10]中.
#include <stdio.h>
#define N 50
#define M 11
void fun(int * a,int * b)
{
    for(int i=0;i<M;i++)
    {
        b[i]=0;
    }
    while(*a)
    {
        if(*a>=0&&*a<=9)
        {
            b[0]++;
        }
        else if(*a>=10&&*a<=19)
        {
            b[1]++;
        }
        else if(*a>=20&&*a<=29)
        {
            b[2]++;
        }
        else if(*a>=30&&*a<=39)
        {
            b[3]++;
        }
        else if(*a>=40&&*a<=49)
        {
            b[4]++;
        }
        else if(*a>=50&&*a<=59)
        {
            b[5]++;
        }
        else if(*a>=60&&*a<=69)
        {
            b[6]++;
        }
        else if(*a>=70&&*a<=79)
        {
            b[7]++;
        }
        else if(*a>=80&&*a<=89)
        {
            b[8]++;
        }
        else if(*a>=90&&*a<=99)
        {
            b[9]++;
        }
        else
        {
            b[10]++;
        }
        a++;
    }
}
double rnd()
{
    static int t=29,c=217,m=1024,r=0;
    r=(r*t+c)%m;
    return ((double)r/m);
}
int main(void)
{
    int age[N],i,d[M];
    for(i=0;i<N;i++)
    {
        age[i]=(int)(115*rnd());
    }
    printf("The roginal data:\n");
    for(i=0;i<N;i++)
    {
        printf((i+1)%10 ==0?"%4d\n":"%4d",age[i]);
    }
    printf("\n\n");
    fun(age,d);
    for(i=0;i<10;i++)
    {
        printf("%4d--%4d:%4d\n",i*10,i*10+9,d[i]);
    }
    printf("Over 100:%4d\n",d[10]);
    return 0;
}
