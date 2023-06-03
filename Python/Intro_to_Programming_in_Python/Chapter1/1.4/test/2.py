import stdio
import sys
import math
import stdarray
import random

n=int(sys.argv[1])

array1=stdarray.create1D(n,0.0)
array2=stdarray.create1D(n,0.0)
array3=[]
for i in range(n):
    array1[i]=i
    array2[i]=i+random.random()*5

for i in range(n):
    array3+=[math.sqrt(math.pow((array1[i]-array2[i]),2))]

for i in range(n):
    stdio.writeln(array3[i])
