#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(4);
    return 0;
}

void meow(int n)
{
    for(int i=0;i<n;i++)
    {
        printf("meow\n");
    }
}