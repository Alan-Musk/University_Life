import stdio
import sys
import math

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

year=int(sys.argv[1])
month=int(sys.argv[2])
day=int(sys.argv[3])

y=year-int((14-month)/12)
x=y+int(y/4)-int(y/100)+int(y/400)
m=month+12*((14-month)/12)-2
d=int((day+x+(31*m)/12)%7)

stdio.writeln(d)

