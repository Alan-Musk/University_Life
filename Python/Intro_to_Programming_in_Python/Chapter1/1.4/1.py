import stdio
import sys
import random
import stdarray

m=int(sys.argv[1])
n=int(sys.argv[2])

perm=stdarray.create1D(n,0)
for i in range(n):
    perm[i]=i+1
for i in range(m):
    r=random.randrange(i,n)
    
    temp=perm[r]
    perm[r]=perm[i]
    perm[i]=temp

for i in range(m):
    stdio.writeln(str(perm[i])+' ')
