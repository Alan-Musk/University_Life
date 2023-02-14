#include <stdio.h>
#define N 2
int main(void)
{
    int temp=0;
    int nums[N][N]={{2,4},{8,10}};
    for(int i=0;i<N-1;i++)
    {
        for(int j=N-1;j>0;j--)
        {
            temp=nums[i][j];
            nums[i][j]=nums[j][i];
            nums[j][i]=temp;
            printf("1\n");
        }
    }
    return 0;
}