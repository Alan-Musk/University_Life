#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int num=get_int("How many scores?");
    int count=0;

    int socres[num];

    for(int i=0;i<num;i++)
    {
        socres[i]=get_int("Socre:");
        count=count+socres[i];
    }

    printf("Avg:%.2f",count/num/1.0 );
    return 0;
}