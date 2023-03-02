import random
import sys
import stdarray
import stdio

def getCoupon(n):
    return random.randrange(0,n)

def collect(n):
    isCollected=stdarray.create1D(n,False)
    count=0
    collectedCount=0
    while collectedCount<n:
        value=getCoupon(n)
        count+=1
        if not isCollected[value]:
            collectedCount+=1
            isCollected[value]=True
    return count

n=int(sys.argv[1])
result=collect(n)
stdio.writeln(result)