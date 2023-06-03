#Compose a code fragment to write the transposition (rows and columns changed) of a two-dimensional array.
import stdarray
import stdio

a=stdarray.create2D(10,3)
b=stdarray.create2D(3,10)
for i in range(10):
    for j in range(3):
        a[i][j]=stdio.readInt()
for i in range(3):
    for j in range(10):
        b[i][j]=a[j][i]
for i in range(3):
    for j in range(10):
        stdio.write(str(b[i][j])+"\t")
    stdio.writeln()