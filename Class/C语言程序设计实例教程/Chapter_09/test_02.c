#include <stdio.h>
#include <stdlib.h>
#define SIZE 2
typedef struct student
{
    int id;
    char name[30];
    int grade1;
    int grade2;
    int grade3;
    double average;
} SD;

int main(void)
{
    FILE * fp;
    SD students[SIZE];
    for(int i=0;i<SIZE;i++)
    {
        printf("请输入学生的学生号:");
        scanf("%d",&students[i].id);
        printf("请输入学生的姓名:");
        scanf("%s",students[i].name);
        printf("请输入学生的第1门成绩:");
        scanf("%d",&students[i].grade1);
        printf("请输入学生的第2门成绩:");
        scanf("%d",&students[i].grade2);
        printf("请输入学生的第3门成绩:");
        scanf("%d",&students[i].grade3);
        students[i].average=(students[i].grade1+students[i].grade2+students[i].grade3)/3.0;
    }
    if((fp=fopen("student","w"))==NULL)
    {
        fprintf(stderr,"文件打开失败");
        exit(EXIT_FAILURE);
    }
    fprintf(fp,"%-10s%-10s%-10s%-10s%-10s%-10s\n","学生","学生号","第一门成绩","第二门成绩","第三门成绩","平均分");
    for(int i=0;i<SIZE;i++)
    {
        fprintf(fp,"%-10s%-10d%-10d%-10d%-10d%-10lf\n",students[i].name,students[i].id,students[i].grade1,students[i].grade2,students[i].grade3,students[i].average);
    }
    fclose(fp);
    return 0;
}