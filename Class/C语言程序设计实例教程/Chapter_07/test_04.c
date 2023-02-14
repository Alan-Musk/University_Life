#include <stdio.h>
#include <stdlib.h>
#define NUM 5
typedef struct worker
{
    int id;
    float salary;
    struct worker * next;
} WK;
void creat(WK * worker,int n);
void list(WK * worker);
void insert(WK * worker);
void delete(WK * worker,int n);
int main(void)
{
    int num=0;//联系删除函数,用户选择删除哪个工号
    WK * wk,* head,*before;
    //定义头链表,由于按照头链表遍历整个链表,故要提前定义.
    head=malloc(sizeof(WK));
    head->id=10;
    head->salary=200;
    head->next=NULL;
    //创建节点,并输入数据
    printf("请输入%d个节点:\n",NUM);
    for(int n=0;n<NUM-1;n++)
    {
        wk=malloc(sizeof(WK));
        creat(wk,n);
        if(head->next==NULL)
        {
            head->next=wk;
            before=wk;
        }
        else
        {
            before->next=wk;
            before=wk;
        }
    }
    //输出数据
    list(head);
    //新增数据
    wk=head;
    //寻找最后一个结构
    while(head->next!=NULL&&wk->next!=NULL)
    {
        wk=wk->next;
    }
    insert(wk);
    //删除节点
    printf("请选择要删除的职工号:");
    scanf("%d",&num);
    delete(head,num);
    list(head);
    return 0;
}
void delete(WK * worker,int n)
{
    WK * father;//使用父节点链接
    //找到要删除的节点
    father=worker;
    while(worker->next!=NULL)
    {
        if(worker->id==n)
        {
            break;
        }
        father=worker;
        worker=worker->next;
    }
    father->next=worker->next;
    free(worker);
}
void insert(WK * worker)
{
    WK * new=malloc(sizeof(WK));
    new->id=worker->id+1;
    printf("请输入职工号%d的薪水:",new->id);
    scanf("%f",&new->salary);
    new->next=NULL;
    worker->next=new;
}
void creat(WK * worker,int n)
{
    worker->id=n+11;

    printf("职工号:%d的薪水为:",worker->id);
    scanf("%f",&worker->salary);
    worker->next=NULL;
}
void list(WK * worker)
{
    do
    {
        printf("职工号:%d的薪水是%f.\n",worker->id,worker->salary);
        worker=worker->next;
    }while(worker->next!=NULL);
    printf("职工号:%d的薪水是%f.\n",worker->id,worker->salary);
}