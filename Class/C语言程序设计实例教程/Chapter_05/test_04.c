#include <stdio.h>
#define ITEM 20
int func(int num);
int main(void)
{
    printf("第%d项是:%d.\n",ITEM,func(ITEM));
    return 0;
}

int func(int num)
{
    if(num<=0)
    {
        return 0;
    }
    else if(num==1)
    {
        return 1;
    }
    else
    {
        return (func(num-1)+func(num-2));
    }
}