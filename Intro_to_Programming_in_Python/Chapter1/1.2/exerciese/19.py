import stdio
import sys
import math

G=9.80665

if len(sys.argv)!=4:
    stdio.writeln('参数有误')
    sys.exit(1)

x=float(sys.argv[1])
v=float(sys.argv[2])
t=float(sys.argv[3])

distance=x+v*t-G*t*t/2.0

stdio.write('经过的距离是:')
stdio.writeln(distance)
