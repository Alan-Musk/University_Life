// 编程题:已知学生的记录由学号和学生成绩构成,N名学生的数据已存入结构体数组a中.
// 请编写函数fun,函数的功能是:找出成绩最高的学生记录,通过形参指针传回主函数(规定只有一个最高分).已给出函数的首部,请完成该函数
#include <stdio.h>
#include <string.h>
#define N 10
typedef struct ss
{
    char num[10];
    int s;
}STU;
void fun(STU a[],STU *s);
int main(void)
{
    STU a[N]={{"A01",81},{"A02",89},{"A03",66},{"A04",87},{"A05",77},{"A06",90},{"A07",79},{"A08",61},{"A09",80},{"A10",71}};
    STU m;
    int i;
    printf("******The original data****\n");
    for(i=0;i<N;i++)
    {
        printf("No=%s Mark:%d\n",a[i].num,a[i].s);
    }
    fun(a,&m);
    printf("The Result\n");
    printf("The top:%s,%d\n",m.num,m.s);
    return 0;
}
void fun(STU a[],STU *s)
{
    int maximum=0;
    for(int i=0;i<N;i++)
    {
        if(a[i].s>maximum)
        {
            maximum=a[i].s;
            strcpy(s->num,a[i].num);
        }
    }
    s->s=maximum;
}