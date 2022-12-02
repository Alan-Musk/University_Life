#include <stdio.h>

int main(void)
{
    int numbers[]={9,3,4,5,6,3,2};

    printf("%i\n",*numbers);
    printf("%i\n",*(numbers+1));
    printf("%i\n",*(numbers+2));
    printf("%i\n",*(numbers+3));
    printf("%i\n",*(numbers+4));
    printf("%i\n",*(numbers+5));
    printf("%i\n",*(numbers+6));


    return;
}