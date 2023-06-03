import sys
import stdarray
import stdio
import stdrandom

class Counter:
    def __init__(self,id,maxCount) -> None:
        self._name=id
        self._maxCount=maxCount
        self._count=0
    
    def increment(self):
        if self._count<self._maxCount:
            self._count+=1
    
    def value(self):
        return self._count
    def __str__(self) -> str:
        return self._name+':'+str(self._count)

def main():
    n=int(sys.argv[1])
    p=float(sys.argv[2])
    heads=Counter('Heads',n)
    tails=Counter('Tails',n)
    for i in range(n):
        if stdrandom.bernoulli(p):heads.increment()
        else:tails.increment()
    stdio.writeln(heads)
    stdio.writeln(tails)

if __name__=='__main__':main()