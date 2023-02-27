// 改错题:给定程序MODI1.C中的函数creatlink的功能是创建带头节点的单向链表
// 并为各节点数据域划分0到m-1的值
// 请改正函数Creatlink中指定部位的错误,使他能得出正确的答案
#include <stdio.h>
#include <stdlib.h>
typedef struct aa
{
    int data;
    struct aa *next;
}NOOE;
NOOE *Creatlink(int n,int m);
int main(void)
{
    NOOE *head;
    head=Creatlink(8,22);
    return 0;
}
NOOE *Creatlink(int n,int m)
{
    NOOE *h=NULL,*p,*s;
    int i;
    p=(NOOE *)malloc(sizeof(NOOE));
    h=p;
    p->next=NULL;
    for(i=1;i<=n;i++)
    {
        s=(NOOE *)malloc(sizeof(NOOE));
        s->data=rand()%m;
        s->next=p->next;
        p->next=s;
        p=p->next;
    }
    return p;
}