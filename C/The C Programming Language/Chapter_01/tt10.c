#include <stdio.h>

int main(void)
{
    int ch;
    while((ch=getchar())!=EOF)
    {
        if(ch=='\t')
        {
            printf("\\t");
        }
        else if(ch=='\\')
        {
            printf("\\\\");
        }
        else if(ch=='\b')
        {
            printf("\\b");
        }
        else
        {
            putchar(ch);
        }
    }
}