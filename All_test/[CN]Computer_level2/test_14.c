// 填空题:给定程序中已建立一个带有头节点的单向链表,链表中的各节点按数据域递增有序链表,函数fun的功能是:删除链表中数据域值相同的节点,使之只保留一个
#include <stdio.h>
#include <stdlib.h>
#define N 8
typedef struct list
{
    int data;
    struct list *next;
}SLIST;
void fun(SLIST *h);
SLIST * creatlist(int *a);
void outlist(SLIST *h);
int main(void)
{
    SLIST *head;
    int a[N]={1,2,2,3,4,4,4,5};
    head=creatlist(a);
    printf("\nThe list before deteting:\n");
    outlist(head);
    fun(head);
    printf("\nThe list after deleting:\n");
    outlist(head);
    return 0;
}
void fun(SLIST *h)
{
    SLIST *p,*q;
    p=h->next;
    if(p!=NULL)
    {
        q=p->next;
        while(q!=NULL)
        {
            if(p->data==q->data)
            {
                p->next=q->next;
                free(q);
                q=p->next;
            }
            else
            {
                p=q;
                q=p->next;
            }
        }
    }
}

SLIST * creatlist(int * a)
{
    SLIST *h,*p,*q;
    int i;
    h=p=(SLIST *)malloc(sizeof(SLIST));
    for(i=0;i<N;i++)
    {
        q=(SLIST *)malloc(sizeof(SLIST));
        q->data=a[i];
        p->next=q;
        p=q;
    }
    p->next=0;
    return h;
}
void outlist(SLIST * h)
{
    SLIST * p;
    p=h->next;
    if(p==NULL)
    {
        printf("\neThe list is NULL!\n");
    }
    else
    {
        printf("\nHead");
        do
        {
            printf("->%d",p->data);
            p=p->next;
        }while(p!=NULL);
        printf("->End\n");
    }
}