import sys
import stdio

if len(sys.argv) !=3:
    stdio.writeln('参数错误')
    sys.exit(1)
n,k=int(sys.argv[1]),int(sys.argv[2])

#牛顿迭代法
x=float(n)
while True:
    y=((k-1)*x+n/pow(x,k-1))/k
    if abs(y-x)<0.000001:
        break
    x=y

stdio.writeln(x)
