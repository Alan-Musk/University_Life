import stdio
import sys
import math

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=float(sys.argv[1])
num2=float(sys.argv[2])
num3=float(sys.argv[3])

if (num1>num2 and num2>num3) or (num1<num2 and num2<num3) :
    stdio.writeln('True')
else :
    stdio.writeln('False')