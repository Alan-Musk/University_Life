import stdio
import sys
import math

n=int(sys.argv[1])

factor=2
while factor*factor<=n:
    if(n%factor) ==0:
        n//=factor
        stdio.write(str(factor)+' ')
    factor+=1

if n>1:
    stdio.writeln(n)