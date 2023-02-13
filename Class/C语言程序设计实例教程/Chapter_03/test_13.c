#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    int square;
    bool isNum;
    for(int i=1;i<100;i++)
    {
        isNum=false;
        for(int j=0;j<1000;j++)
        {
            square=j*j;
            if(i>0&&i<10)
            {
                if(i==square%10)
                {
                    isNum=true;
                }
            }
            else
            {
                if((i%10==square%10)&&((i%100-i%10)/10==(square%100-square%10)/10))
                {
                    isNum=true;
                }
            }
        }
        if(isNum)
        {
            printf("%d是同构数.\n",i);
        }
    }

    return 0;
}