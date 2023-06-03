import stdarray
import stdio

def readBool2D():
    m=stdio.readInt()
    n=stdio.readInt()
    a=stdarray.create2D(m,n,False)
    for i in range(m):
        for j in range(n):
            a[i][j]=stdio.readBool()
    return a

readBool2D()
