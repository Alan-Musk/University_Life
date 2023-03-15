// 回形取数
#include <stdio.h>
int a[201][201];
int vis[201][201];
int main(void)
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    int x=1,y=1;
    printf("%d",a[1][1]);
    vis[1][1]=1;
    int sum=1;
    while(sum<n*m)
    {
        while(x+1<=n&&vis[x+1][y]==0)
        {
            printf("%d ",a[++x][y]);
            vis[x][y]=1;
            sum++;
        }
        while(y+1<=m&&vis[x][y+1]==0)
        {
            printf("%d ",a[x][y++]);
            vis[x][y]=1;
            sum++;
        }
        while(x-1>=1&&vis[x-1][y]==0)
        {
            printf("%d ",a[--x][y]);
            vis[x][y]=1;
            sum++;
        }
        while(y-1>=1&&vis[x][y-1]==0)
        {
            printf("%d ",a[x][--y]);
            vis[x][y]=1;
            sum++;
        }
    }
    return 0;
}