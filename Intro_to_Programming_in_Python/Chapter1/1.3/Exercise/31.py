import stdio
import random
import math
x=1
y=1

while (x*x+y*y) >1.0:
    x=2.0*random.random()
    y=2.0*random.random()
a=2.0*x*math.sqrt((1.0-x*x-y*y))
b=2.0*math.sqrt((1.0-x*x-y*y))
c=1.0-2.0*(x*x+y*y)
stdio.writeln('a='+str(a))
stdio.writeln('b='+str(b))
stdio.writeln('c='+str(c))
