// 程序通过定义学生结构体变量,存储了学生的学号,姓名和3门课的成绩,所有学生数据均以二进制方式输出到文件中.
// 函数fun的功能是从形参filename所指的文件中读入学生数据,并按照学号,从小到大排序后,再用二进制方式把排序后的学生数据输出到filename所指的文件中,覆盖原来的文件内容
#include <stdio.h>
#define N 5
typedef struct student
{
    long sno;
    char name[10];
    float score[3];
}STU;
void fun(char * filename)
{
    FILE * fp;
    int i,j;
    STU s[N],t;
    fp=fopen(filename,"rb");
    fread(s,sizeof(STU),N,fp);
    fclose(fp);
    for(i=0;i<N-1;i++)
    {
        for(j=i+1;j<N;j++)
        {
            if(s[i].sno>s[j].sno)
            {
                t=s[i];
                s[i]=s[j];
                s[j]=t;
            }
        }
    }
    fp=fopen(filename,"wb");
    fwrite(s,sizeof(STU),N,fp);
    fclose(fp);
}
int main(void)
{
    STU t[N]={{10005,"MaChao",{91,92,77}},{10003,"CaoKai",{75,60,88}},{10002,"LiSi",{85,70,78}},{10004,"FangFang",{90,82,87}},{10001,"ZhangSan",{95,80,88}}};
    STU ss[N];
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
    fun("student.dat");
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