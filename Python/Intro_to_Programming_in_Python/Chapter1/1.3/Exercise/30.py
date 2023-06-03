import stdio
import sys
import random
x=1
y=1
while (x*x+y*y)>1.0:
    x=2.0*random.random()
    y=2.0*random.random()
stdio.writeln(str(x)+'  '+str(y))

