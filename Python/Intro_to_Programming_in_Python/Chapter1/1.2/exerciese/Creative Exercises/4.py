import stdio
import sys
import math
import random

u=random.random()
v=random.random()
w=math.sin(2*math.pi*v) * (-2*math.log(u))**(1/2)

stdio.writeln('w='+str(w))