#include <stdio.h>

int main(void)
{
    //(1):字符型和整型都可以
    //(2):printf("%d\n%d",c1,c2);
    //(3):不可以。C语言中整型变量和字符型变量不能在任何情况下互相代替。整型变量是用来存储整数值的，字符型变量则是用来存储单个字符的。
    //它们的存储方式、取值范围和数据类型都不同。
    int c1,c2;
    printf("请输入第一个字符:");
    c1=getchar();
    while(getchar()!='\n')
    {
        continue;
    }
    printf("请输入第二个字符:");
    c2=getchar();
    while(getchar()!='\n')
    {
        continue;
    }
    putchar(c1);
    putchar(c2);
    printf("\n%c\n%c\n",c1,c2);
    return 0;
}