#include <stdio.h>
#include <math.h>

struct dot
{
    int x;
    int y;
};
int main(void)
{
    struct dot dot1,dot2;
    double distance;
    int x,y;
    printf("请输入一个点的坐标(x,y):");
    scanf("%d %d",&x,&y);
    dot1.x=x;
    dot1.y=y;
    printf("请输入一个点的坐标(x,y):");
    scanf("%d %d",&x,&y);
    dot2.x=x;
    dot2.y=y;
    distance=sqrt(pow(dot1.x-dot2.x,2)+pow(dot1.y-dot2.y,2));
    printf("两点的距离是:%lf.\n",distance);
    return 0;
}