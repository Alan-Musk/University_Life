import sys
import stdarray
import stddraw
import stdrandom
import stdstats
import stdio

class Histogram:
    def __init__(self,n) -> None:
        self._freq=stdarray.create1D(n,0)
    def addDataPoint(self,i):
        self._freq[i]+=1
    def draw(self):
        stddraw.setYscale(0,max(self._freq))
        stdstats.plotBars(self._freq)

def main():
    n=int(sys.argv[1])
    p=float(sys.argv[2])
    trials=int(sys.argv[3])
    histogram=Histogram(n+1)
    stddraw.setCanvasSize(500,200)
    for t in range(trials):
        heads=stdrandom.binomial(n,p)
        histogram.addDataPoint(heads)
        
    histogram.draw()
    stddraw.show()   
if __name__=='__main__':main()