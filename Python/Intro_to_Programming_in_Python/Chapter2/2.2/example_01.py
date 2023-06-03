import math
import sys
import stdio

def pdf(x,mu=0.0,sigma=1.0):
    x=float(x-mu)/sigma
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/sigma

def cdf(z,mu=0.0,sigma=1.0):
    z=float(z-mu)/sigma
    if z<-8.0:return 0.0
    if z>+8.0:return 1.0
    total=0.0
    term=2
    i=3
    while total!=total+term:
        total+=term
        term*=z*z/i
        i+=2
    return 0.5+total*pdf(z)

def main():
    z=float(sys.argv[1])
    mu=float(sys.argv[2])
    sigma=float(sys.argv[3])
    stdio.writeln(cdf(z,mu,sigma))

if __name__=='__main__':main()