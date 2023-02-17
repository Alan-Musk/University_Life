#include <stdio.h>

int main(void)
{
    for(float celsius=0;celsius<=300;celsius+=20)
    {
        printf("%3f %6.1f\n",celsius,celsius/(5.0/9.0)+32.0);
    }
}