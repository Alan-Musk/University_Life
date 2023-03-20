#include <stdio.h>
#define N 50
#define M 11

void fun(int * a,int * b);
double rnd(void)
{
    static int  t=29,c=217,m=1024,r=0;
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
    printf("The original data:\n");
    for(i=0;i<N;i++)
    {
        printf((i+1)%10==0?"%4d\n":"%4d",age[i]);
    }
    printf("\n\n");
    fun(age,d);
    for(i=0;i<10;i++)
    {
        printf("%4d--%4d:  %4d\n",i*10,i*10+9,d[i]);
    }
    printf("Over 100: %4d\n",d[10]);
    return 0;
}
void fun(int * a,int * b)
{
    for(int i=0;i<M;i++)
    {
        b[i]=0;
    }
    int num=0;
    for(int i=0;i<N;i++)
    {
        num=a[i];
        if(num>=0&&num<=9)
        {
            b[0]++;
        }
        else if(num>=10&&num<=19)
        {
            b[1]++;
        }
        else if(num>=20&&num<=29)
        {
            b[2]++;
        }
        else if(num>=30&&num<=39)
        {
            b[3]++;
        }
        else if(num>=40&&num<=49)
        {
            b[4]++;
        }
        else if(num>=50&&num<=59)
        {
            b[5]++;
        }
        else if(num>=60&&num<=69)
        {
            b[6]++;
        }
        else if(num>=70&&num<=79)
        {
            b[7]++;
        }
        else if(num>=80&&num<=89)
        {
            b[8]++;
        }
        else if(num>=90&&num<=100)
        {
            b[9]++;
        }
        else if(num>100)
        {
            b[10]++;
        }
    }
}