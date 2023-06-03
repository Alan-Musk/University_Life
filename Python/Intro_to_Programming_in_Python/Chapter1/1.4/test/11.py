# Compose a code fragment to transpose a square two-dimensional array b[][] in place without creating a second array.
import stdio
import sys
import stdarray

n=int(sys.argv[1])
a=stdarray.create2D(n,n)
for i in range(n):
    for j in range(n):
        a[i][j]=stdio.readInt()
stdio.writeln("之前:")
for i in range(n):
    for j in range(n):
        stdio.write(str(a[i][j])+"\t")
    stdio.writeln()
stdio.writeln("之后:")
for i in range(n):
    for j in range(i,n):
        temp=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=temp
for i in range(n):
    for j in range(n):
        stdio.write(str(a[i][j])+"\t")
    stdio.writeln()