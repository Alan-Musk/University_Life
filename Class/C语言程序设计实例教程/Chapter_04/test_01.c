#include <stdio.h>

int main(void)
{
    int temp;
    int nums[10]={3,46,74,1,45,5345,3,543,65,76};
    for(int n=9;n>=0;n--)
    {
        for(int j=0;j<n;j++)
        {
            if(nums[j+1]>nums[j])
            {
                temp=nums[j+1];
                nums[j+1]=nums[j];
                nums[j]=temp;
            }
        }
    }
    for(int n=0;n<10;n++)
    {
        printf("%d ",nums[n]);
    }
    printf("\n");
    return 0;
}