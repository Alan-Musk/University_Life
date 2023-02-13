#include <stdio.h>
#define FSIZE 2
#define SSIZE 3
int main(void)
{
    int nums[FSIZE][SSIZE];
    printf("请输入%d次整数\n",FSIZE*SSIZE);
    for(int n=0;n<FSIZE;n++)
    {
        for(int j=0;j<SSIZE;j++)
        {
            scanf("%d",&nums[n][j]);
        }
    }
}