import stdio
import sys
import math 

if len(sys.argv) !=4:
    stdio.writeln('参数错误')
    sys.exit(1)

R=float(sys.argv[1])
G=float(sys.argv[2])
B=float(sys.argv[3])
C=0
M=0
Y=0
K=0
if R!=0 and G!=0 and B!=0:
    w=max(R/255,G/255,B/255)
    C=(w-(R/255))/w
    M=(w-(G/255))/w
    Y=(w-(B/255))/w
    K=1-w


stdio.writeln(C)
stdio.writeln(M)
stdio.writeln(Y)
stdio.writeln(K)

