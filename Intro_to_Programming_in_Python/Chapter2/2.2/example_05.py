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

def main():
    a=stdarray.readFloat1D()
    stdio.writef('   mean  %7.3f\n',mean(a))
    stdio.writef('std dev %7.3f\n',stddev(a))

if __name__ == '__main__':main()