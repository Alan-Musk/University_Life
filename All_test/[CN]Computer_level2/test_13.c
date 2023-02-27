// 编程题:请编一个函数fun,函数的功能是使实型数保留2位小数,并对第三位进行四舍五入
#include <stdio.h>

float fun(float h);
int main(void)
{
    float a;
    printf("Enter a:");
    scanf("%f",&a);
    printf("The original data is :");
    printf("%f\n\n",a);
    printf("The result:%f\n",fun(a));
    return 0;
}
float fun(float h)
{
    h=(int)((h+0.005)*100)
    h/=100;
    return h;
}