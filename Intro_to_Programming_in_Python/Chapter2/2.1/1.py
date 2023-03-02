import sys
import stdio

def harmonic(n):
    total=0.0
    for i in range(1,n+1):
        total+=1.0/i
    return total

for i in range(1,len(sys.argv)):
    arg=int(sys.argv[i])
    value=harmonic(arg)
    stdio.writeln(value)