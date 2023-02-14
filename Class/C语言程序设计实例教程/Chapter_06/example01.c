// 杨辉三角
#include <stdio.h>
void getdata(int (*p)[18],int m);
void outdata(int p[][18],int m);

int main(void)
{
    int a[18][18],n;
    printf("请从键盘上输入杨辉三角的行数:");
    scanf("%d",&n);
    while(n<=1||n>18)
    {
        scanf("%d",&n);
    }
    getdata(a,n);
    outdata(a,n);
    return 0;
}
void getdata(int (*p)[18],int m)
{
    int i,j;
    for(i=0;i<m;i++)
    {
        p[i][i]=1;//对角线为1
        p[i][0]=1;//第一列为1
    }
    //从第三行开始
    for(i=2;i<m;i++)
    {
        for(j=1;j<i;j++)
        {
            p[i][j]=p[i-1][j-1]+p[i-1][j];
        }
    }
}
//输出
void outdata(int p[][18],int m)
{
    int i,j;
    for(i=0;i<m;i++)
    {
        for(j=0;j<=i;j++)
        {
            printf("%6d",p[i][j]);
        }
        printf("\n");
    }
    getchar();
}