#include <stdio.h>

int main(void)
{
    if((getchar()!=EOF)==1)
    {
        printf("getchar()!=EOF is equal to 1.");
    }
    else
    {
        printf("getchar()!=EOF is equal to 0.");
    }
}