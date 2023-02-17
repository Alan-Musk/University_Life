// 实现直方图,垂直方向
#include <stdio.h>

#define IN 1 //定义单词内
#define OUT 0 //定义单词外
#define MAXHIST 15 //直方图的最大长度
#define MAXWORD 11 //单词的最大长度

int main(void)
{
    int c,i,j,nc,state;
    int maxvalue;       //vl[]数组中的最大值
    int ovflow;         //超过限制的单词
    int wl[MAXWORD];    //单词长度计数
    state=OUT;
    nc=0;
    ovflow=0;
    for(i=0;i<MAXWORD;i++)
    {
        wl[i]=0;
    }
    while((c=getchar())!=EOF)
    {
        if(c==' '||c=='\t'||c=='\n')
        {
            state=OUT;
            if(nc>0)
            {
                if(nc<MAXWORD)
                {
                    ++wl[nc];
                }
                else
                {
                    ++ovflow;
                }
            }
            nc=0;
        }
        else if(state==OUT)
        {
            state=IN;
            nc=1;
        }
        else
        {
            nc++;
        }
    }
    maxvalue=0;
    for(i=1;i<MAXWORD;i++)
    {
        if(wl[i]>maxvalue)
        {
            maxvalue=wl[i];
        }
    }
    for(i=MAXHIST;i>0;i--)
    {
        for(j=1;j<MAXWORD;++j)
        {
            if(wl[j]*MAXHIST/maxvalue>=i)
            {
                printf("  *  ");
            }
            else
            {
                printf("    ");
            }
        }
        putchar('\n');
    }
    for(i=1;i<MAXWORD;++i)
    {
        printf("%4d ",i);
    }
    putchar('\n');
    for(i=1;i<MAXWORD;i++)
    {
        printf("%4d ",wl[i]);
    }
    putchar('\n');
    if(ovflow>0)
    {
        printf("There are %d words >=%d.\n",ovflow,MAXWORD);
    }
}