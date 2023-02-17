#include <stdio.h>

int main(void)
{
    int ch;
    while((ch=getchar())!=EOF)
    {
        printf("EOF is equal to %d.\n",ch);
    }
}