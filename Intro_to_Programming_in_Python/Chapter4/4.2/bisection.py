import sys
import stdio
import gaussian

def invert(f,y,lo,hi,delta=0.00000001):
    mid=(lo+hi)/2.0
    if (hi-lo)<delta:
        return mid
    if f(mid)>y:
        return invert(f,y,lo,mid,delta)
    else:
        return invert(f,y,mid,hi,delta)
    
def main():
    y=float(sys.argv[1])
    x=invert(gaussian.cdf,y,-8.0,8.0)
    stdio.writef('%.3f\n',x)

if __name__=='__main__':main()
