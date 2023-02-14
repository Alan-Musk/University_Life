#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 50

struct student
{
    char name[50];
    int id;
    float chinese_grade;
    float math_grade;
    float english_grade;
    float average_grade;
    int rank;
};
//求平均值
void average(struct student students[],int n);
//排序
void rank_students(struct student students[],int n);
//输出
void print_students(struct student students[],int n);
int main(void)
{
    struct student students[MAX_STUDENTS];
    int n;
    printf("Enter the number of students(up to %d):",MAX_STUDENTS);
    scanf("%d",&n);

    for(int i=0;i<n;i++)
    {
        printf("Enter data for student %d:\n",i+1);
        printf("Name:");
        scanf("%s",students[i].name);
        printf("ID:");
        scanf("%d",&students[i].id);
        printf("Chinese grade:");
        scanf("%f",&students[i].chinese_grade);
        printf("Math grade:");
        scanf("%f",&students[i].math_grade);
        printf("English grade:");
        scanf("%f",&students[i].english_grade);
    }
    average(students,n);
    rank_students(students,n);
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (students[j].average_grade > students[i].average_grade)
            {
                struct student temp = students[i];
                students[i] = students[j];
                students[j] = temp;
            }
        }
    }
    print_students(students,n);
    return 0;
}
void print_students(struct student students[],int n)
{
    printf("%-20s%-10s%-10s%-10s%-10s%-10s%-10s\n","Name","ID","Chinese","Math","English","Average","Rank");
    for(int i=0;i<n;i++)
    {
        printf("%-20s%-10d%-10.2f%-10.2f%-10.2f%-10.2f%-10d\n", students[i].name, students[i].id,
        students[i].chinese_grade, students[i].math_grade, students[i].english_grade, students[i].average_grade, students[i].rank);
    }
}
void rank_students(struct student students[],int n)
{
    int ranks[MAX_STUDENTS]={0};
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(students[j].average_grade>students[i].average_grade)
            {
                ranks[i]++;
            }
            else if(students[i].average_grade>students[j].average_grade)
            {
                ranks[j]++;
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        students[i].rank=ranks[i]+1;
    }
}
void average(struct student students[],int n)
{
    for(int i=0;i<n;i++)
    {
        students[i].average_grade=(students[i].chinese_grade + students[i].math_grade + students[i].english_grade) / 3.0;
    }
}
