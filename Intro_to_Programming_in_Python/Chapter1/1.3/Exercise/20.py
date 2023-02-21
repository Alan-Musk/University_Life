import stdio
import sys
import math

n=int(sys.argv[1])

s=''
while n>0:
    s=str(n%10)+s
    n//=10
    

stdio.writeln(s)