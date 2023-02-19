import stdio
import sys
import math
import random

n=int(sys.argv[1])
num1=random.random()
maximum=0.0
sum=0.0
minimum=1.0
for i in range(n):
    number=random.random()
    stdio.writeln(number)
    sum+=number
    if number>maximum:
        maximum=number
    elif number<minimum:
        minimum=number

stdio.writeln(num1)
stdio.writeln("平均值是:"+str(sum/n))
stdio.writeln('最大值是'+str(maximum))
stdio.writeln('最小值是'+str(minimum))