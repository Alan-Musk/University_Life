// 高精度加法 输入两个整数 a和b,输出两个数的和,a和b都不超过100位
#include <stdio.h>
#include <string.h>

#define SIZE 101

int main()
{
    char a[SIZE],b[SIZE],sum[SIZE];
    int carry=0,i,j,k;

    //读入数字字符串
    scanf("%s%s",a,b);
    int len1=strlen(a);
    int len2=strlen(b);

    //逐位相加
    for(i=len1-1,j=len2-1,k=0;i>=0||j>=0||carry;i--,j--,k++)
    {
        int num1=i >=0 ? a[i]-'0' : 0;
        int num2=j >=0 ? b[j]-'0' : 0;
        int digit_sum=num1+num2+carry;
        sum[k]=digit_sum%10+'0';
        carry=digit_sum/10;
    }

    //反转字符串并输出
    for(i=0,j=k-1;i<j;i++,j--)
    {
        char temp=sum[i];
        sum[i]=sum[j];
        sum[j]=temp;
    }
    printf("%s\n",sum);
    return 0;
}