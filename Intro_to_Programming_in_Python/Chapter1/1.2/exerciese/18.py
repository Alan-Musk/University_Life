import stdio
import sys
import math

if len(sys.argv)!=2 :
    stdio.writeln('参数有误')
    sys.exit(1)

t=float(sys.argv[1])

stdio.writeln(math.sin(2*t)+math.sin(3*t))