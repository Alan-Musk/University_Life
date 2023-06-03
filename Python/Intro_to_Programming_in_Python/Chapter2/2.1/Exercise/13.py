import math
import sys
import stdio

def two_stars(x1,y1,x2,y2):
    x1=math.radians(x1)
    y1=math.radians(y1)
    x2=math.radians(x2)
    y2=math.radians(y2)
    x=x2-x1
    y=y2-y1
    temp=math.sin(y/2.0)**2+math.cos(y1)*math.cos(y2)*(math.sin(x/2.0))**2
    return 2*math.asin(temp**0.5)

x1=float(sys.argv[1])
y1=float(sys.argv[2])
x2=float(sys.argv[3])
y2=float(sys.argv[4])

stdio.writeln(two_stars(x1,y1,x2,y2))

    