// 自行车停放
#include <stdio.h>
const int N=200010;
struct node
{
    int data;
    int preid;
    int nextid;
}nodes[N];
int now;//当前节点
int locate[N];      //locate[x]=now,值为x的节点的位置在nodes[now]
void init()
{
    nodes[0].nextid=1;
    nodes[1].preid=0;
    now=2;
}
void insert(int k,int x)
{
    nodes[now].data=x;
    locate[x]=now;
    nodes[now].nextid=nodes[k].nextid;
    nodes[now].preid=k;
    nodes[nodes[k].nextid].preid=now;
    nodes[k].nextid=now;
    now++;
}
int main()
{
    int n,a;
    scanf("%d%d",&n,&a);
    init();
    insert(0,a);
    n--;
    while(n--)
    {
        int x,y,z;
        scanf("%d%d%d",&x,&y,&z);
        int temp=locate[y];
        if(z==0)
        {
            insert(nodes[temp].preid,x);
        }
        else
        {
            insert(temp,x);
        }
    }
    for(int i=nodes[0].nextid;i!=1;i=nodes[i].nextid)
    {
        printf(" %d",nodes[i].data);
    }
    return 0;
}