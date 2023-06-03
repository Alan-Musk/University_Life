import stdio
import sys
import time

n=int(sys.argv[1])
end=time.time()+10
factor=2
while factor*factor<=n:
    start=time.time()
    if start == end:
        stdio.writeln('10s了')
        stdio.writeln(factor)
        break
    if(n%factor) ==0:
        n//=factor
        stdio.write(str(factor)+' ')
    factor+=1

if n>1:
    stdio.writeln(n)