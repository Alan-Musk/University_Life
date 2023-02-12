#include <stdio.h>

int main(void)
{
    int grade;
    printf("Please input your final grade:");
    scanf("%d",&grade);
    if(grade>=90)
    {
        printf("优!\n");
    }
    else if(grade>=80&&grade<90)
    {
        printf("良.\n");
    }
    else if(grade>=60&&grade<80)
    {
        printf("中.\n");
    }
    else if(grade<60)
    {
        printf("差.\n");
    }
    return 0;
}