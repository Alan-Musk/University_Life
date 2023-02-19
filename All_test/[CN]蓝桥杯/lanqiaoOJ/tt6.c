// 统计优秀率和及格率
#include <stdio.h>

int main(void)
{
    int grade;
    float normal=0;
    float good=0;
    int number;
    scanf("%d",&number);
    for(int i=0;i<number;i++)
    {
        scanf("%d",&grade);
        if(grade>=60)
        {
            normal++;
        }
        if(grade>=85)
        {
            good++;
        }
    }
    printf("%d%%\n",(int)(normal*100/number*(1.0)));
    printf("%d%%",(int)(good*100/number*(1.0)));
    return 0;
}