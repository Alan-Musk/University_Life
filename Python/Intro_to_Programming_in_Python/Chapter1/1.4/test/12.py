import stdio
import sys
import stdarray
m=int(sys.argv[1])
n=int(sys.argv[2])
a=stdarray.create2D(m,n)
b=stdarray.create2D(n,m)
for i in range(m):
    for j in range(n):
        a[i][j]=stdio.readInt()
for i in range(n):
    for j in range(m):
        b[i][j]=a[j][i]
for i in range(n):
    for j in range(m):
        stdio.write(str(b[i][j])+"\t")
    stdio.writeln()