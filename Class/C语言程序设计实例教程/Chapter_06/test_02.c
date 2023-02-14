#include <stdio.h>
#define SIZE 6
int main(void)
{
    int nums[SIZE]={56,53,43,234,42,32};
    for(int i=0;i<SIZE/2;i++)
    {
        printf("第%d组的和是%d.\n",i+1,nums[i]+nums[SIZE-i-1]);
    }
    return 0;
}