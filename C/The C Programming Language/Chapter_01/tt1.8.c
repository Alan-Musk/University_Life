#include <stdio.h>

int main(void)
{
    int spaceSum=0,nSum=0,tSum=0;
    int ch;
    while((ch=getchar())!=EOF)
    {
        if(ch==' ')
        {
            spaceSum++;
        }
        else if(ch=='\n')
        {
            nSum++;
        }
        else if(ch=='\t')
        {
            tSum++;
        }
    }
    printf("spaceSum=%d,nSum=%d,tSum=%d.\n",spaceSum,nSum,tSum);
    return 0;
}