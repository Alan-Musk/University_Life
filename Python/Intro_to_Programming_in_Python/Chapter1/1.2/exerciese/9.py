import math
import sys
import stdio

b=float(sys.argv[1])
c=float(sys.argv[2])

discriminant=b*b-4.0*c
# IndexError: list index out of range
d=sqrt(discriminant)

stdio.writeln((-b+d)/2.0)
stdio.writeln((-b-d)/2.0)
