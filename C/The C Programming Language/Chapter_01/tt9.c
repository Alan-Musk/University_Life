#include <stdio.h>

int main(void)
{
    int ch;
    int last='a';
    while((ch=getchar())!=EOF)
    {
        if(ch!=' ')
        {
            putchar(ch);
        }
        else if(ch==' ')
        {
            if(last==' ')
            {
                continue;
            }
            putchar(ch);
        }
        last=ch;
    }
}