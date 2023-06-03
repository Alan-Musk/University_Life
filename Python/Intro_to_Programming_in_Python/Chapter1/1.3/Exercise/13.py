import stdio
import sys
import math

if len(sys.argv) !=2:
    stdio.writeln('参数有误')
    sys.exit(1)

n=int(sys.argv[1])

pow=1
if n<0:
    sys.exit(1)
else :
    while pow<=n:
        stdio.writeln(pow)
        pow*=2