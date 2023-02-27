// 编程题:请编写函数fun,函数的功能是:统计一行字符串中单词的个数,作为函数值返回.
// 一行字符串在主函数中输入,规定所有单词有小写字母组成,单词之间由小写字母组成,单词之间由若干个空格隔开,一行的开始没有空格
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define N 80
// 目标函数
int fun(char *s);
int main(void)
{
    char line[N];
    int num=0;
    printf("Enter a string:\n");
    fgets(line,N,stdin);
    num=fun(line);
    printf("The number of word is:%d\n",num);
    return 0;
}
int fun(char *s)
{
    int sum=0;
    for(int i=0;*(s+i)!='\n';i++)
    {
        if(i==0)
        {
            if(*(s+i)!=' ')
            {
                sum++;
            }
            continue;
        }
        else
        {
            if(!(isalpha(*(s+i-1)))&&isalpha(*(s+i)))
            {
                sum++;
            }
        }
    }
    return sum;
}