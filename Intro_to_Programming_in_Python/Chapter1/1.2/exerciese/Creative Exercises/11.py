import stdio
import sys
import math

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])

maximum=max(num1,num2,num3)
minimum=min(num1,num2,num3)
stdio.writeln(minimum)
stdio.writeln(num1+num2+num3-maximum-minimum)
stdio.writeln(maximum)

