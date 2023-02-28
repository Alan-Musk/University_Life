// 编程题:请编写一个函数fun,它的功能是,找出一维整数数组元素最大的值和它所在的下标,最大的值和它所在的下标通过形参传回.数组元素中的值已在主函数中赋予
#include <stdio.h>
#include <stdlib.h>
void fun(int a[],int n,int *max,int *d);
int main(void)
{
    int i,x[20],max,index,n=10;
    for(i=0;i<n;i++)
    {
        x[i]=rand()%50;
        printf("%4d",x[i]);
    }
    printf("\n");
    fun(x,n,&max,&index);
    printf("Max=%5d,Index=%4d\n",max,index);
    return 0;
}
void fun(int a[],int n,int *max,int *index)
{
    *max=a[0];
    *index=0;
    for(int i=0;i<n;i++)
    {
        if(*max<a[i])
        {
            *max=a[i];
            *index=i;
        }
    }
}