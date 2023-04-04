import sys
import random
import stdio

n=int(sys.argv[1]) #测试次数
wins=0  # 赢的次数

for i in range(0,n):
    # 生成奖品的位置
    prize=random.randrange(0,3)
    # 选择
    choice=random.randrange(0,3)
    # 主持人指出一个
    reveal=random.randrange(0,3)
    while(reveal==choice)or(reveal==prize):
        reveal=random.randrange(0,3)
    # 不换
    # if(prize==choice):
    #     wins+=1
    # 换了
    other=0+1+2-reveal-choice
    if other==prize:
        wins+=1

fractionWon=float(wins)/float(n)

stdio.writeln(fractionWon)

