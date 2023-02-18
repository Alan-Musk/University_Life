import stdio
import sys
import math

if len(sys.argv) !=5:
    stdio.writeln('参数错误')
    sys.exit(1)

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])


x1=math.radians(x1)
y1=math.radians(y1)
x2=math.radians(x2)
y2=math.radians(y2)

d=math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
d=math.degrees(d)

d=60.0*d

stdio.writeln(d)