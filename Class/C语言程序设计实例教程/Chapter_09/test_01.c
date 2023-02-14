#include <stdio.h>
#include <ctype.h>
int main(void)
{
    FILE * fp;
    char st[81];
    char ch;
    int i=0;
    while((ch=getchar())!='!')
    {
        st[i]=toupper(ch);
        i++;
    }
    if((fp=fopen("test.txt","w"))!=NULL)
    {
        fprintf(fp,"%s",st);
    }
    return 0;
}