import stdarray
import stdio
import random

def f(a,num):
    maximum=max(a) 
    minimum=min(a)
    for i in range(num):
        a[i]=(a[i]-minimum)/(maximum/minimum)
    return a

num=stdio.readInt()
a=stdarray.create1D(num,0.0)
for i in range(num):
    a[i]=random.random()*100
for i in range(num):
    stdio.writeln(a[i])
f(a,num)
for i in range(num):
    stdio.writeln(a[i])