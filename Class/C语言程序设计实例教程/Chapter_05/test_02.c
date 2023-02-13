#include <stdio.h>
#include <stdbool.h>
bool isOdd(int n);
int main(void)
{
    int x;
    printf("please enter a number:");
    scanf("%d",&x);
    if(isOdd(x))
    {
        printf("the number is an odd.");
    }
    else
    {
        printf("the number is an even.");
    }
    return 0;
}
bool isOdd(int n)
{
    if(n%2)
    {
        return true;
    }
    else
    {
        return false;
    }
}