#include <stdio.h>
#include <string.h>
#define SIZE 80
char * s_gets(char * st,int n);
int main(void)
{
    char ch[2][SIZE];
    printf("请输入两句话:\n");
    for(int n=0;n<2;n++)
    {
        s_gets(ch[n],SIZE);
    }
    for(int n=0;n<2;n++)
    {
        printf("第%d句话为:%s\n",n+1,ch[n]);
    }

    return 0;
}

char * s_gets(char * st,int n)
{
    char * ret_val;
    char * find;
    ret_val=fgets(st,n,stdin);
    if(ret_val)
    {
        find=strchr(st,'\n');
        if(find)
        {
            *find='\0';
        }
        else
        {
            while(getchar()!='\n')
            {
                continue;
            }
        }
    }
    return ret_val;
}