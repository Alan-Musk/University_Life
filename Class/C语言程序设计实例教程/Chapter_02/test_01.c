#include <stdio.h>

int main(void)
{
    double num=3.4;
    printf("转换成整型后:%d\n",(int)num);
    printf("转换成长整型后:%ld\n",(long int)num);
    printf("转换成单精度输出:%f\n",(float)num);
    return 0;
}