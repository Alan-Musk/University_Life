// 实例49 动态链表的建立及常用操作--输出学习的信息
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct student
{
    int num;
    char name[20];
    struct student *next;
}ST;

int main(void)
{
    ST *head,*p,*s,new;
    head=NULL;//初始化头指针
    //创建一个空链表,并将头指针动态开辟存储空间
    head=malloc(sizeof(ST));
    if(head==NULL)
    {
        printf("没有足够的内存!");
        return 1;
    }
    head->next=NULL;
    head->num=0;
    //在链表中插入节点
    p=head;//p先指向头指针
    do
    {
        printf("请输入学生的学号为:\n");
        scanf("%d",&new.num);
        if(new.num==0)//学号为0时,循环结束
        {
            break;
        }
        printf("请输入学生的姓名:");
        scanf("%s",new.name);
        s=malloc(sizeof(ST));
        if(s==NULL)
        {
             printf("没有足够的内存!");
            return 1;
        }
        strcpy(s->name,new.name);
        s->num=new.num;
        s->next=NULL;
        p->next=s;
        p=s;
        printf("节点已经插入,成功!\n");
    }while(1);
    p=head->next;
    while(p!=NULL)
    {
        printf("学生的学号为:%d 姓名为:%s\n",p->num,p->name);
        p=p->next;
    }
    getchar();
}