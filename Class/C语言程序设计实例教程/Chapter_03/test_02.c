#include <stdio.h>

int main(void)
{
    float high,radius;
    printf("请输入高和半径的长度:");
    scanf("%f %f",&high,&radius);
    printf("圆柱体的体积是:%.2f",radius*radius*3.14*high);
    return 0;
}