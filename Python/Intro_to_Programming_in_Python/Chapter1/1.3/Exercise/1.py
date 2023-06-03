import stdio
import sys
import math

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=sys.argv[1]
num2=sys.argv[2]
num3=sys.argv[3]

if num1==num2==num3 :
    stdio.writeln('euqal')
else:
    stdio.writeln('not euqal')