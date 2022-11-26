#include <stdio.h>
#include <cs50.h>
#include <string.h>

int string_length(string na);
int main(void)
{
    string name=get_string("What is your name?");
    int length=strlen (name);

    printf("%i\n",length);
}

int string_length(string na)
{
    int num=0;
    while(na[num]!='\0')
    {
        num++;
    }

    return num;
}