import stdio
import sys
import math

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=float(sys.argv[1])
num2=float(sys.argv[2])
num3=float(sys.argv[3])

x=num3-num1
y=1/2*math.log((1+math.sin(num2))/(1-math.sin(num2)))

stdio.writeln('坐标为('+str(x)+','+str(y)+')')