import stdio
import sys
import math

if len(sys.argv) !=3:
    stdio.writeln('参数有误')
    sys.exit(1)

m=int(sys.argv[1])
d=int(sys.argv[2])

if m<=0 or m>12 or d<=0 or d>31:
    stdio.writeln('日期输入有误')
    sys.exit(1)

days=(m-1)*30+d

if (days>=80) and (days<=170):
    stdio.writeln('True')
else:
    stdio.writeln('False')