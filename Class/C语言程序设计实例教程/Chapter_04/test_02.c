#include <stdio.h>
#include <stdbool.h>
#define SIZE 3
int main(void)
{
    bool isNum=false;
    int nums[SIZE];
    puts("请输入是个整数:");
    for(int n=0;n<SIZE;n++)
    {
        scanf("%d",&nums[n]);
    }
    for(int n=0;n<SIZE;n++)
    {
        if(nums[n]==3)
        {
            isNum=true;
            printf("输入历史里包含3,是第%d次输入的.\n",n+1);
        }
    }
    if(isNum==false)
    {
        printf("输入历史不包含3.\n");
    }
    return 0;
}