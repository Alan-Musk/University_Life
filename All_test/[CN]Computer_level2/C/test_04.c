// 填空题:程序通过定义学生结构体变量,存储了学生的学号,姓名和3门课的成绩.所有学生数据均以二进制方式输出到文件中.
// 函数fun的功能是重写形参filename所指文件中最后一个学生的数据,即用新的学生数据覆盖该学生原来的数据,其他学生的数据不变
#include <stdio.h>
#define N 5
typedef struct student
{
    long sno;
    char name[10];
    float score[3];
}STU;
void fun(char * filename,STU n);
int main(void)
{
    STU t[N]={{10001,"MaChao",{91,92,77}},{10002,"CaoKai",{75,60,88}},{10003,"LiSi",{85,70,78}},{10004,"FangFang",{90,82,87}},{10005,"ZhangSan",{95,80,88}}};
    STU n={10006,"ZhaoSi",{55,70,68}},ss[N];
    int i,j;
    FILE * fp;
    fp=fopen("student.dat","wb");
    fwrite(t,sizeof(STU),N,fp);
    fclose(fp);
    fp=fopen("student.dat","rb");
    fread(ss,sizeof(STU),N,fp);
    fclose(fp);
    printf("\nThe original data:\n\n");
    for(j=0;j<N;j++)
    {
        printf("\nNo:%ld Name:%-8s    Scores:  ",ss[j].sno,ss[j].name);
        for(i=0;i<3;i++)
        {
            printf("%6.2f",ss[j].score[i]);
        }
        printf("\n");
    }
    fun("student.dat",n);
    printf("\nThe data after modifing:\n\n");
    fp=fopen("student.dat","rb");
    fread(ss,sizeof(STU),N,fp);
    fclose(fp);
    for(j=0;j<N;j++)
    {
        printf("\nNo:%ld Name:%-8s    Scores:  ",ss[j].sno,ss[j].name);
        for(i=0;i<3;i++)
        {
            printf("%6.2f",ss[j].score[i]);
        }
        printf("\n");
    }
    return 0;
}
void fun(char * filename,STU n)
{
    FILE *fp;
    fp=fopen(filename,"rb+");
    fseek(fp,-(long)sizeof(STU),SEEK_END);
    fwrite(&n,sizeof(STU),1,fp);
    fclose(fp);
}