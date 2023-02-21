import stdio
import sys
import math
import random

stake=int(sys.argv[1])  #赌注
goal=int(sys.argv[2]) #目标
trials=int(sys.argv[3])
times=int(sys.argv[4])

bets=0
wins=0
for t in range(trials):
    time=0
    cash=stake
    while (cash>0) and (cash<goal):
        if time==times:
            stdio.writeln('break了')
            break;
        else:
            time+=1
        bets+=1
        if random.randrange(0,2)==0:
            cash+=1
        else:
            cash-=1
    if cash==goal:
        wins+=1

stdio.writeln(str(100*wins//trials)+'%wins')
stdio.writeln('Avg # bets:'+str(bets//trials))
