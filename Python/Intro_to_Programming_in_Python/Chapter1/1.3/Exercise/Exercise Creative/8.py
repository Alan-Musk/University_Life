import time
import stdio
import math

def math_exp(a):
    before=time.time()
    i=0
    while (time.time())-before<10:
        i+=1
        math.exp(a)
    stdio.writeln("math.exp运算到"+str(i))

def first(a,n):
    before=time.time()
    i=0
    while (time.time())-before<10:
        i+=1
        term=1.0
        for k in range(1,n+1):
            term*=a/i
    stdio.writeln("方法1运算到"+str(i))

def second(a):
    before=time.time()
    i=0
    while (time.time())-before<10:
        i+=1
        term=1.0
        total=0.0
        n=1
        while total!=total+term:
            total+=term
            term=1.0
            for w in range(1,n+1):
                term*=a/w
            n+=1
    stdio.writeln("方法2运算到"+str(i))

def third(a):
    before=time.time()
    i=0
    while (time.time())-before<10:
        i+=1
        term=1.0
        total=0.0
        n=1
        while total!=total+term:
            total+=term
            term*=a/n
            n+=1
    stdio.writeln("方法3运算到"+str(i))
a=int(input())
math_exp(a)
first(a,100)
second(a)
third(a)