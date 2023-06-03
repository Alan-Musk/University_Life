import stdio
import sys
import math

if len(sys.argv) != 3:
    stdio.writeln('参数错误')
    sys.exit(1)

x=float(sys.argv[1])
y=float(sys.argv[2])

PolarX=math.hypot(x,y)
PolarY=math.atan2(y,x)

stdio.writeln('PolarX        ='+str(PolarX))      
stdio.writeln('PolarY        ='+str(PolarY))      