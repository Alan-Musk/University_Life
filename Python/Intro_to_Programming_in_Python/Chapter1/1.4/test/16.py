import stdio
import sys
import random
import stdarray
import stddraw

if len(sys.argv)< 5 and sys.argv[2]!=sys.argv[3]:
    stdio.writeln("参数设置有误")
    exit()
row1=int(sys.argv[1])
col1=int(sys.argv[2])
row2=int(sys.argv[3])
col2=int(sys.argv[4])
a=stdarray.create2D(row1,col1,0.0) # 矩阵A
b=stdarray.create2D(row2,col2,0.0) # 矩阵B
c=stdarray.create2D(row2,col1,0.0)
# 给矩阵A赋值
for i in range(row1):
    for j in range(col1):
        a[i][j]=stdio.readInt()
# 给矩阵B赋值
for i in range(row2):
    for j in range(col2):
        b[i][j]=stdio.readInt()
# A*B=C
for i in range(row2):
    for j in range(row2):
        for k in range(col1):
            c[i][j]+=a[i][k]*b[k][j]

# 输出
stdio.writeln(c)