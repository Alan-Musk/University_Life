import stdio
import sys
import math
import random

num1=random.random()
num2=random.random()
num3=random.random()
num4=random.random()
num5=random.random()

stdio.writeln(num1)
stdio.writeln(num2)
stdio.writeln(num3)
stdio.writeln(num4)
stdio.writeln(num5)
stdio.writeln("平均值是:"+str((num1+num2+num3+num4+num5)/5))
stdio.writeln('最大值是'+str(max(num1,num2,num3,num4,num5)))
stdio.writeln('最小值是'+str(min(num1,num2,num3,num4,num5)))