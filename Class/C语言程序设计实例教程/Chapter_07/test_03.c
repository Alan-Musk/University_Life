#include <stdio.h>
#define NUM 16
struct person
{
    int before;
    int after;
};

int main(void)
{
    int sum=0;//监视剩余总和
    int number=0;//赋值
    struct person people[NUM];
    for(int i=0;i<NUM;i++)
    {
        people[i].before=i+1;
        people[i].after=i%3+1;
    }
    do
    {
        sum=0;
        //清除为3的数
        for(int i=0;i<NUM;i++)
        {
            if(people[i].after==3)
            {
                people[i].after=0;
            }
        }
        //重新组合1,2的数,并监控剩余的数量
        for(int i=0;i<NUM;i++)
        {
            if(people[i].after==1||people[i].after==2)
            {
                people[i].after=number%3+1;
                number++;
                sum++;
            }
        }
    }while(sum>2);
    sum=1;
    for(int i=0;i<NUM;i++)
    {
        if(people[i].after>0)
        {
            printf("剩余的第%d个数,之前的序号为:%d.\n",sum,people[i].before);
            sum++;
        }
    }
}