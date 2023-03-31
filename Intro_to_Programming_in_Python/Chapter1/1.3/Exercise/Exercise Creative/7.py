import stdio
import sys
import random
import math

def sinx(x):
    total=0.0
    term=x
    n=1
    while total!=total+term:
        total+=term
        term*=(x*x)/((n+1)*(n+2))*-1
        n+=2
    return total

def cosx(x):
    total=0
    term=1
    n=1
    while total!=total+term:
        total+=term
        term*=(-1*x*x)/(n*(n+1))
        n+=2
    return total


x=float(input("请输入一个弧长"))
stdio.writeln(sinx(x))
stdio.writeln(cosx(x))


