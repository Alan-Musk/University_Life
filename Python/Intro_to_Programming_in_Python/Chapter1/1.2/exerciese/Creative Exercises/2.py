import stdio
import sys
import math

if len(sys.argv) !=3:
    stdio.writeln('参数有误')
    exit(1)

t=float(sys.argv[1])
v=float(sys.argv[2])
if t>=50 or v >120 or v<3:
    stdio.writeln('公式')
    exit(1)

stdio.writeln('温度(Temperature)='+str(t))
stdio.writeln('风速(Wind speed)='+str(v))
stdio.writeln('体感温度(Wind chill)='+str(35.74+0.6215*t+(0.4275*t-35.75)*v**0.16))