#include <stdio.h>

int main(void)
{
    int num1,num2;
    char ch;
    printf("请输入要处理的运算:");
    ch=getchar();
    while(getchar()!='\n')
    {
        continue;
    }
    printf("请输入两个数字:");
    scanf("%d %d",&num1,&num2);
    switch (ch)
    {
        case '+':   printf("%d+%d=%d",num1,num2,num1+num2); break;
        case '-':   printf("%d-%d=%d",num1,num2,num1-num2); break;
        case '*':   printf("%d*%d=%d",num1,num2,num1*num2); break;
        case '/':   printf("%d/%d=%d",num1,num2,num1/num2); break;
        default:    printf("输入有误!");
    }
    return 0;
}