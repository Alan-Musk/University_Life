import stdio
import sys
import example_06
import stdarray
import stddraw
import test
import stdrandom
import math

n=int(sys.argv[1])
trials=int(sys.argv[2])

freq=stdarray.create1D(n+1,0)
for t in range(trials):
    heads=stdrandom.binomial(n,0.5)
    freq[heads]+=1

norm=stdarray.create1D(n+1,0.0)
for i in range(n+1):
    norm[i]=1.0*freq[i]/trials

phi=stdarray.create1D(n+1,0.0)
stddev=math.sqrt(n)/2.0
for i in range(n+1):
    phi[i]=test.pdf(i,n/2.0,stddev)

stddraw.setCanvasSize(1000,400)
stddraw.setYscale(0,1.1*max(max(norm),max(phi)))
example_06.plotBars(norm)
example_06.plotLines(phi)
stddraw.show(20000)

