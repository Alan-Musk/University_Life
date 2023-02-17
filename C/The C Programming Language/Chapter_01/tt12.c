#include <stdio.h>
#define IN 1
#define OUT 0

int main(void)
{
    int ch;
    int state;
    while((ch=getchar())!=EOF)
    {
        if(ch=='\n'||ch==' '||ch=='\t'||ch=='.'||ch==',')
        {
            state=OUT;
        }
        else if(state==OUT)
        {
            printf("\n");
            state=IN;
            putchar(ch);
        }
        else
        {
            putchar(ch);
        }
    }
}