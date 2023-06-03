import sys
import stdarray
import stdio
import stdrandom
import threesum
from stopwatch import Stopwatch

def timeTrial(n):
    a=stdarray.create1D(n,0)
    for i in range(n):
        a[i]=stdrandom.uniformInt(-1000000,1000000)
    watch=Stopwatch()
    count=threesum.countTriples(a)
    return watch.elapsedTime()

n=int(sys.argv[1])
while True:
    previous=timeTrial(n//2)
    current=timeTrial(n)
    ratio=current/previous
    stdio.writef('%7d %4.2f\n',n,ratio)
    n*=2