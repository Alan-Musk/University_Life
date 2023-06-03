import stdio
import sys
import math

if len(sys.argv) != 4:
    stdio.writeln('参数有误')
    sys.exit(1)

t=int(sys.argv[1])
p=float(sys.argv[2])
r=float(sys.argv[3])

stdio.writeln((math.e*p)**(t*r))
