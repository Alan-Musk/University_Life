#include <stdio.h>
#include <stdbool.h>

int months[]={0,31,28,31,30,31,30,31,31,30,31,30,31};

bool check(char s[10])
{
    for(int i=0;i+2<10;i++)
    {
        if(s[i]+1==s[i+1]&&s[i]+2==s[i+2])
        {
            return true;
        }
    }
    return false;
}

int main(void)
{
    int y=2022,m=1,d=1;
    int cnt=0;
    for(int i=0;i<365;i++)
    {
        char s[10];
        sprintf(s,"%04d%02d%02d",y,m,d);
        if(check(s)) cnt++;
        d++;
        if(d>months[m]){d=1;m++;}
    }
    printf("%d",cnt);
}