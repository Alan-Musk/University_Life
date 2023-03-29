import stdio
import sys
import random
n=int(sys.argv[1])
sum=0
w=e=n=s=0
while True:
    ran=random.randrange(1,5)
    sum+=1
    if ran==1:
        w+=1
        if w>10:
            break
    elif ran==2:
        e+=1
        if e>10:
            break
    elif ran==3:
        n+=1
        if n>10:
            break
    else:
        s+=1
        if s>10:
            break
stdio.writeln(sum)
