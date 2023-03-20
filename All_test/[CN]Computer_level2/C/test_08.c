// 程序通过定义学生结构体变量,存储了学生的学号,姓名和3门课的成绩.函数fun的功能是将形参a中的数据进行修改
// 把修改后的数据作为函数值返回主函数进行输出
#include <stdio.h>
#include <string.h>

struct student
{
    long sno;
    char name[10];
    float score[3];
};
struct student fun(struct student a);
int main(void)
{
    struct student s={10001,"ZhangSan",{95,80,88}};
    struct student t;
    int i;
    printf("\n\nThe original data:\n");
    printf("\nNo:%ld Name:%s\nScores: ",s.sno,s.name);
    for(i=0;i<3;i++)
    {
        printf("%6.2f",s.score[i]);
    }
    printf("\n");
    t=fun(s);
    printf("\n\nThe original data:\n");
    printf("\nNo:%ld Name:%s\nScores: ",t.sno,t.name);
    for(i=0;i<3;i++)
    {
        printf("%6.2f",t.score[i]);
    }
    printf("\n");
    return 0;
}
struct student fun(struct student a)
{
    int i;
    a.sno=10002;
    strcpy(a.name,"LiSi");
    for(i=0;i<3;i++)
    {
        a.score[i]+=1;
    }
    return a;
}