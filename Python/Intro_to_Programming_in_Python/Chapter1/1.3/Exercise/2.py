import math
import sys
import stdio

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

if a==0:
    stdio.writeln('二次方程首项为0')
    d=-c/b
    stdio.writeln('根为'+str(d))
elif (b*b-4.0*a*c)<0:
    stdio.writeln('判别式小于0')
    stdio.writeln('该方程没有根')
else:
    discriminant=b*b-4.0*a*c
    d=math.sqrt(discriminant)
    stdio.writeln((-b+d)/(2.0*a))
    stdio.writeln((-b-d)/(2.0*a))


