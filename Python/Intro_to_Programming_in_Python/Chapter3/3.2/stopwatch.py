import math
import sys
import stdio
import time

class Stopwatch:
    def __init__(self) -> None:
        self._start=time.time()
    def elapsedTime(self):
        return time.time()-self._start

def main():
    n=int(sys.argv[1])
    
    total1=0.0
    watch1=Stopwatch()
    for i in range(1,n+1):
        total1+=1**3
    time1=watch1.elapsedTime()

    total2=0.0
    watch2=Stopwatch()
    for i in range(1,n+1):
        total2+=i*i*i
    time2=watch2.elapsedTime()

    stdio.writeln(total1/total2)
    stdio.writeln(time1/time2)

if __name__=='__main__':
    main()