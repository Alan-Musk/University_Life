import stdio
import sys
import math

if len(sys.argv) !=3:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=float(sys.argv[1])
num2=float(sys.argv[2])

if num1>0 and num1<1 and num2 >0 and num2<1:
    stdio.writeln('True')
else:
    stdio.writeln('False')