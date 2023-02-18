import stdio
import math
import sys

if len(sys.argv) !=3:
    stdio.writeln('参数有误')
    sys.exit(1)

x=float(sys.argv[1])
y=float(sys.argv[2])
distance=math.hypot(x,y)

stdio.write('距离为')
stdio.writeln(distance)
