// 单词分析
#include <stdio.h>

int main(void)
{
    int letters[26]={0};
    int max=0;
    char ch;
    while((ch=getchar())!='\n')
    {
        letters[ch-'a']++;
    }
    for(int i=0;i<26;i++)
    {
        if(letters[i]>max)
        {
            max=i;
        }
    }
    printf("%c\n%d",max+'a',letters[max]);
    return 0;
}