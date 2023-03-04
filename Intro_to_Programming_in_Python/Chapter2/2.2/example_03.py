import math
import random
import sys
import stdio

def uniformInt(lo,hi):
    return random.randrange(lo,hi)

def uniformFloat(lo,hi):
    return random.uniform(lo,hi)

def bernoulli(p=0.5):
    return random.random()< p

def binomial(n,p=0.5):
    heads=0
    for i in range(n):
        if bernoulli(p):heads+=1
    return heads

def discrete(a):
    r=uniformFloat(0.0,sum(a))
    subtotal=0.0
    for i in range(len(a)):
        subtotal=+a[i]
        if subtotal>r :return i
    return i

def main():
    trials=int(sys.argv[1])
    for i in range(trials):
        stdio.writef('%2d ',uniformInt(10,100))
        stdio.writef('%8.5f ',uniformFloat(10.0,99.0))
        stdio.writef('%5s ',bernoulli(0.5))
        stdio.writef('%2d ',binomial(100,0.5))
        stdio.writef('%1d ',discrete([5,3,1,1]))
        stdio.writeln()

if __name__ =='__main__': main()
        
