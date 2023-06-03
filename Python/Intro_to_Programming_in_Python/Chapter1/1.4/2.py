import stdio
import sys
import random
import stdarray

n=int(sys.argv[1])

count=0
collectedCount=0
isCollected=stdarray.create1D(n,False)

while collectedCount < n:
    value=random.randrange(0,n)
    count+=1
    if not isCollected[value]:
        collectedCount+=1
        isCollected[value]=True
stdio.writeln(count)