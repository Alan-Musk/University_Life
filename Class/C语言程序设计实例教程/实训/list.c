#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "list.h"

bool delete_number(DIC *user, int *n)
{
    int num;
    printf("请输入要删除的学号:");
    scanf("%d", &num);
    for (int i = 0; i < *n; i++)
    {
        if (user->id == num)
        {
            // 这里说明一下:由于教材的诱导,使用结构数组,在清除为0后,还需消耗内存将后面的数组移到前面去
            move_array(user, *n - i);
            (*n)--;
            return true;
        }
        else
        {
            user += 1;
        }
    }
    return false;
}

void move_array(DIC *user, int n)
{
    for (int i = 0; i < n; i++)
    {
        user[i]=user[i+1];
    }
}
//清除缓存
void clean(void)
{
    while (getchar() != '\n')
    {
        continue;
    }
}

// 存储
bool tofile(DIC *user, int n)
{
    FILE *fp;
    char fileName[SIZE];
    printf("请输入要输入的文件名:");
    scanf("%s", fileName);
    if ((fp = fopen(fileName, "w")) == NULL)
    {
        fprintf(stderr, "文件打开失败.");
        return false;
    }
    fprintf(fp, "%d\n", n);
    for (int j = 0; j < n; j++)
    {
        fprintf(fp, "%d  %s  %s  %ld  ", user->id, user->name, user->gender, user->number);
        for (int i = 0; i < M; i++)
        {
            fprintf(fp, "%.1f  ", user->grades[i]);
        }
        fprintf(fp, "  %.2f\n", user->total);
        user += 1;
    }
    fclose(fp);
    return true;
}
//排序
void sort(DIC *user, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (user[j].total > user[j + 1].total)
            {
                DIC temp = user[j];
                user[j] = user[j + 1];
                user[j + 1] = temp;
            }
        }
    }
}

// 按学号输出数据
bool show_person(DIC *user, int n)
{
    int student_number;
    printf("请输入要查询的学号:");
    scanf("%d", &student_number);
    for (int i = 0; i < n; i++)
    {
        if (user->id == student_number)
        {
            printf("学号:%d    姓名:%s    性别:%s    电话:%ld      %d门课程:", user->id, user->name, user->gender, user->number, M);
            for (int i = 0; i < M; i++)
            {
                printf("%.1f  ", user->grades[i]);
            }
            printf("  总分:%.2f\n", user->total);
            return true;
        }
        else
        {
            user += 1;
        }
    }
    return false;
}

// 菜单
int menu(void)
{
    int choose;
    printf("+-----------------------------------------------+\n");
    printf("|       Student Manger Information System       |\n");
    printf("+-----------------------------------------------+\n");
    printf("|               1.Insert Record                 |\n");
    printf("|               2.Change Record                 |\n");
    printf("|               3.Delete Record                 |\n");
    printf("|               4.Sort Record                   |\n");
    printf("|               5.Print All Record              |\n");
    printf("|               6.Print individual Record       |\n");
    printf("|               7.Save Record                   |\n");
    printf("|               8.Exit Record                  |\n");
    printf("+-----------------------------------------------+\n");
    printf("|        Please input num to select(1-8)        |\n");
    printf("+-----------------------------------------------+\n");
    scanf("\n%d", &choose);
    return choose;
}
// 显示所有数据
void show_all(DIC *user, int n)
{
    printf("学号    姓名    性别    电话       %d门课程         总成绩\n", M);
    for (int i = 0; i < n; i++)
    {
        printf("%d  %s  %s  %ld    ", (user + i)->id, (user + i)->name, (user + i)->gender, (user + i)->number);
        for (int j = 0; j < M; j++)
        {
            printf("%.1f  ", (user + i)->grades[j]);
        }
        printf("%.2f", (user + i)->total);
        printf("\n");
    }
}
// 给结构数组添加一个项
bool add_data(DIC *user, int n)
{
    (user + n)->total = 0;
    printf("请输入学号 姓名 性别 电话号码 %d门课程分数(以空格分隔):", M);
    scanf("%d %s %s %ld", &(user + n)->id, (user + n)->name, (user + n)->gender, &(user + n)->number);
    // 获取成绩
    for (int i = 0; i < M; i++)
    {
        scanf("%f", &(user + n)->grades[i]);
        (user + n)->total += (user + n)->grades[i];
    }
    // 如果都为正常值,返回真,传入总数就增加1
    if (((user + n)->name) != NULL && ((user + n)->number) != 0 && ((user + n)->id) != 0 && ((user + n)->gender) != NULL && ((user + n)->grades[0]) != 0)
    {
        return true;
    }
    return false;
}

//  操作:修改
bool revise_number(DIC *user, int n)
{
    int num;
    printf("请输入要修改的学号:");
    scanf("%d", &num);
    for (int i = 0; i < n; i++)
    {
        if (user->id == num)
        {
            printf("学号:%d    姓名:%s    性别:%s    电话:%ld      %d门课程:", user->id, user->name, user->gender, user->number, M);
            for (int i = 0; i < M; i++)
            {
                printf("%.1f  ", user->grades[i]);
            }
            printf("  总分:%.2f\n", user->total);
        }
        else if ((i + 1) == n)
        {
            printf("学号;%d不存在.\n", num);
            return false;
        }
        else
        {
            user += 1;
        }
    }
    printf("请输入姓名 性别 电话号码 %d门课程分数(以空格分隔):", M);
    scanf("%s %s %ld", user->name, user->gender, &user->number);
    for (int i = 0; i < M; i++)
    {
        scanf("%f", &user->grades[i]);
    }
    if ((user->name) != NULL && (user->number) != 0 && (user->id) != 0 && (user->gender) != NULL && (user->grades[0]) != 0)
    {
        return true;
    }
    return false;
}
// 导入数据库
bool openFile(DIC *user, int *n)
{
    FILE *fp;
    char fileName[SIZE];
    // 打开文件
    printf("请输入传入的数据库:");
    scanf("%s", fileName);
    if ((fp = fopen(fileName, "r")) == NULL)
    {
        printf("该数据库不存在.");
        return false;
    }
    // 传入数据
    fscanf(fp, "%d", n); // 传入总数
    for (int i = 0; i < *n; i++)
    {
        fscanf(fp, "%d %s %s %ld", &user->id, user->name, user->gender, &user->number);
        for (int j = 0; j < M; j++)
        {
            fscanf(fp, "%f", &user->grades[j]);
        }
        fscanf(fp, "%f", &user->total);
        user += 1;
    }
    return true;
}