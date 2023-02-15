#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#include "list.h"

bool add_data(DIC * user,int n)
{
    printf("请输入通讯录的姓名:");
    s_gets((user+n)->name,SIZE);
    printf("请输入通讯录的电话号码:");
    scanf("%ld",&(user+n)->number);
    clean();
    if(((user+n)->name)!=NULL&&((user+n)->number)!=0)
    {
        return true;
    }
    return false;
}

void show_all(DIC * user,int n)
{
    for(int i=0;i<n;i++)
    {
         printf("用户%s\t号码:%ld.\n",(user+i)->name,(user+i)->number);
    }
}
bool search_name(DIC * user,int n)
{
    char name[SIZE];
    printf("请输入要查询的姓名:");
    s_gets(name,SIZE);
    for(int i=0;i<n;i++)
    {
        if(strcmp(name,user->name)==0)
        {
             printf("找到:用户%s\t号码:%ld.\n",user->name,user->number);
             return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
bool search_number(DIC * user,int n)
{
    long int num;
    printf("请输入要删除的号码:");
    scanf("%ld",&num);
    for(int i=0;i<n;i++)
    {
        if((long int)user->number==num)
        {
            printf("找到:用户%s\t号码:%ld.\n",user->name,user->number);
            return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
bool delete_number(DIC * user,int * n)
{
    long int num;
    printf("请输入要删除的号码:");
    scanf("%ld",&num);
    for(int i=0;i<*n;i++)
    {
        if((long int)user->number==num)
        {
            //这里说明一下:由于教材的诱导,使用结构数组,在清除为0后,还需消耗内存将后面的数组移到前面去
            move_array(user,*n-i);
            (*n)--;
            return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
bool delete_name(DIC * user,int * n)
{
    char name[SIZE];
    printf("请输入要删除的姓名:");
    s_gets(name,SIZE);
    for(int i=0;i<*n;i++)
    {
        if(strcmp(name,user->name)==0)
        {
            //这里说明一下:由于教材的诱导,使用结构数组,在清除为0后,还需消耗内存将后面的数组移到前面去
            move_array(user,*n-i);
            (*n)--;
            return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
void move_array(DIC * user,int n)
{
    for(int i=0;i<n;i++)
    {
        strcpy(user->name,(user+1)->name);
        user->number=(user+1)->number;
        user++;
    }
}
char menu(void)
{
    char ch;
    printf("************************\n");
    printf("a)输入             b)显示所有数据\n");
    printf("c)按照姓名删除      d)按照号码删除\n");
    printf("e)按照姓名查询      f)按照号码查询\n");
    printf("g)按照姓名修改      h)按照号码修改\n");
    printf("i)排序             k)存储记录(存入文件)\n");
    printf("q)退出\n");
    printf("************************\n");
    ch=getchar();
    clean();
    ch=tolower(ch);
    return ch;
}
char * s_gets(char * st,int n)
{
    char * ret_val;
    char * find;
    ret_val=fgets(st,n,stdin);
    if(ret_val)
    {
        find=strchr(st,'\n');
        if(find)
        {
            *find='\0';
        }
        else
        {
            clean();
        }
    }
    return ret_val;
}
void clean(void)
{
    while(getchar()!='\n')
    {
        continue;
    }
}

//修改
bool revise_name(DIC * user,int n)
{
    char name[SIZE];
    printf("请输入要修改的姓名:");
    s_gets(name,SIZE);
    for(int i=0;i<n;i++)
    {
        if(strcmp(name,user->name)==0)
        {
             printf("姓名修改为:");
             s_gets(user->name,SIZE);
             printf("号码修改为:");
             scanf("%ld",&user->number);
             return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
void tofile(DIC * user,int n)
{
    FILE * fp;
    char fileName[SIZE];
    printf("请输入要输入的文件名:");
    s_gets(fileName,SIZE);
    if((fp=fopen(fileName,"a+"))==NULL)
    {
        fprintf(stderr,"文件打开失败.");
        exit(EXIT_FAILURE);
    }
    for(int i=0;i<n;i++)
    {
        fprintf(fp,"用户%s\t号码:%ld.\n",(user+i)->name,(user+i)->number);
    }
    fclose(fp);
}
bool revise_number(DIC * user,int n)
{
    long int num;
    printf("请输入要删除的号码:");
    scanf("%ld",&num);
    for(int i=0;i<n;i++)
    {
        if((long int)user->number==num)
        {
             printf("姓名修改为:");
             s_gets(user->name,SIZE);
             printf("号码修改为:");
             scanf("%ld",&user->number);
             return true;
        }
        else
        {
            user+=i;
        }
    }
    return false;
}
void sort(DIC *user, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (strcmp(user[j].name, user[j + 1].name) > 0) {
                DIC temp = user[j];
                user[j] = user[j + 1];
                user[j + 1] = temp;
            }
        }
    }
}