#include <stdio.h>

int main(void)
{
    int nums[12]={23,24,321,543,1,1,1,3451,3213,543,76,435};
    int sums[12];
    for(int i=0;i<12;i++)
    {
        if(i==0)
        {
            sums[i]=nums[11]+nums[0]+nums[1];
        }
        else if(i==11)
        {
            sums[i]=nums[i]+nums[i-1]+nums[0];
        }
        else
        {
            sums[i]=nums[i]+nums[i-1]+nums[i+1];
        }
    }
    int min=sums[0];
    for(int i=1;i<12;i++)
    {
        if(sums[i]<min)
        {
            min=sums[i];
        }
    }
    printf("最小值为%d.\n",min);
}