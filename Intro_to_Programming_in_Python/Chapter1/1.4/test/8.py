import stdio
import sys
import random
import stdarray

n=int(sys.argv[1])

SUITS=['Clubs','Diamonds','Hearts','Spades']
RANKS=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
CARDS=[]

for i in RANKS:
    for k in SUITS:
        CARDS+=[i+' of '+k]

# 混排
for i in range(len(CARDS)):
    r=random.randrange(i,len(CARDS))
    temp=CARDS[i]
    CARDS[i]=CARDS[r]
    CARDS[r]=temp

# 输出
for i in range(n*5):
    stdio.writeln(CARDS[i])

