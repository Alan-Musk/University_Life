import stdio
import sys
import math

stdio.writeln('log2n\t\tn\t\tnlogen\t\tn2\t\tn3\t\t2n')
n=2
sum=1
while n<=2048:
    stdio.write(str(math.log(n,2))+'\t\t'+str(n)+'\t\t'+str(n*math.log(n))+'\t\t'+str(n*n)+'\t\t'+str(n*n*n)+'\t\t')
    for i in range(n):
        sum*=2
    stdio.writeln(str(sum))
    n*=2