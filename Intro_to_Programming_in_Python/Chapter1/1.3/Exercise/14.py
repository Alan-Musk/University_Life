import stdio
import sys
import math

if len(sys.argv) != 4:
    stdio.writeln('参数有误')
    sys.exit(1)

t=int(sys.argv[1])  #投资年数
p=float(sys.argv[2]) #本金
r=float(sys.argv[3]) #年利率
#将年利率转换为月利率
mon_rate=r/12
#将投资年数转换为月份
months=t*12
#计算每月还款额
month=(p*mon_rate)/(1-(1+mon_rate)**(-months))

remain_balance=p
for i in range(months):
    #计算每月的利息
    month_interest=remain_balance*mon_rate
    #计算每月的本金偿还额
    month_principal=month-month_interest
    #更新剩余本金
    remain_balance-=month_principal
    #输出
    stdio.writeln(str(round(month,2))+'\t\t'+str(remain_balance))

