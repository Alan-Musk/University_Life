// 本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
// 小蓝每天都锻炼身体。
// 正常情况下，小蓝每天跑1 千米。如果某天是周一或者月初（1
// 日），为了激励自己，小蓝要跑2千米。如果同时是周一或月初，
// 小蓝也是跑2千米。
// 小蓝跑步已经坚持了很长时间，从2000年 1月1日周六（含）到
// 2020年10月1 日周四（含）。请问这段时间小蓝总共跑步多少千
// 米？

#include <stdio.h>
int main(void)
{
    int months[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    int year,month,day;
    int ans=6;//是周六,
    int cnt=0;//公里数
    for(year=2000;year<=2020;year++)
    {
        if((year%4==0&&year%100!=0)||year%400==0)
        {
            months[2]=29;
        }
        else
        {
            months[2]=28;
        }
        for(month=1;month<=12;month++)
        {
            for(day=1;day<=months[month];day++)
            {
                cnt++;
                if(ans==8)
                {
                    ans=1;
                }
                if(ans==1||day==1)
                {
                    cnt++;
                }
                ans++;
                if(year==2020&&month==10&&day==1)
                {
                    printf("%d",cnt);
                }
            }
        }
    }
    return 0;
}