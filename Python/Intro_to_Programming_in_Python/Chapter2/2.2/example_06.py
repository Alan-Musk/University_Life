import math
import stddraw
import stdarray
import stdio

def mean(a):
    return sum(a)/float(len(a))

def var(a):
    mu=mean(a)
    total=0.0
    for x in a:
        total+=(x-mu) *(x-mu)
    return total/(len(a)-1)

def stddev(a):
    return math.sqrt(var(a))

def plotPoints(a):
    n=len(a)
    stddraw.setXscale(0,n-1)
    stddraw.setPenRadius(1.0/(3.0*n))
    for i in range(n):
        stddraw.point(i,a[i])

def plotLines(a):
    n=len(a)
    stddraw.setXscale(0,n-1)
    stddraw.setPenRadius(0.0)
    for i in range(1,n):
        stddraw.line(i-1,a[i-1],i,a[i])

def plotBars(a):
    n=len(a)
    stddraw.setXscale(0,n-1)
    for i in range(n):
        stddraw.filledRectangle(i-0.25,0.0,0.5,a[i])

def main():
    a=stdarray.readFloat1D()
    stdio.writef('   mean  %7.3f\n',mean(a))
    stdio.writef('std dev %7.3f\n',stddev(a))

if __name__ == '__main__':main()