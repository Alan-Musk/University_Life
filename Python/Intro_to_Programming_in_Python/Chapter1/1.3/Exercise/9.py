import stdio
import sys

n=int(sys.argv[1])
rular='1'
stdio.writeln(rular)
for i in range(2,n+1):
    rular=rular+' '+str(i)+' '+rular
    stdio.writeln(rular)