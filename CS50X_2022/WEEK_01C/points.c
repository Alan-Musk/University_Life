#include <cs50.h>
#include <stdio.h>

int main(void)
{
    const int mine=2;
    int points = get_int("How many points did you lose?");

    if(points>mine)
    {
        printf("You lost more than me.\n");
    }
    else if(points<mine)
    {
        printf("You lost fewer than me.\n");
    }
    else
    {
        printf("You lost the same number of points as me\n");
    }
    return 0;
}