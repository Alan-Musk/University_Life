import sys
import stdio
from charge import Charge

x=float(sys.argv[1])
y=float(sys.argv[2])
c1=Charge(.51,.63,21.3)
c2=Charge(.13,.94,81.9)
v1=c1.potentialAt(x,y)
v2=c2.potentialAt(x,y)
stdio.writef('potential at (%.2f,%.2f) duo to\n',x,y)
stdio.writeln('   '+str(c1)+'and')
stdio.writeln('   '+str(c2))
stdio.writef('is %.2e\n',v1+v2)