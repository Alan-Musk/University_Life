#include <stdio.h>
#include <string.h>
#include <cs50.h>

void draw(int n);

int main(void)
{
    int height=get_int("Height:");

    draw(height);

    return 0;
}

void draw(int n)
{
    if(n<=0)
    {
        return;
    }
    draw(n-1);

    for(int i=0;i<n;i++)
    {
        printf("#");
    }
    printf("\n");
}