import stdio
import sys
import math
import random
if len(sys.argv) !=3 :
    stdio.writeln('参数有误')
    sys.exit(1)

num1=int(sys.argv[1])
num2=int(sys.argv[2])
goal=int(random.randrange(num1,num2))

stdio.writeln(goal)