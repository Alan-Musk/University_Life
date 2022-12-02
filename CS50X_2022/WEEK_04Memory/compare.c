#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string first=get_string("First:");
    string second=get_string("Second:");

    printf("%p\n",first);
    printf("%p\n",second);
    return 0;
}
