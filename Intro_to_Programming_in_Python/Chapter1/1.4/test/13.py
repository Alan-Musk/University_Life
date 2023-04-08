# Compose a program that computes the product of two square matrices of boolean values, using the or operation instead of + and the and operation instead of *.
import stdio
import stdarray

n=5
bool1=stdarray.create2D(n,n,False)
bool2=stdarray.create2D(n,n,True)
# 通过给input.txt中的数取余,设置基础data
for i in range(n):
    for j in range(n):
        a=stdio.readInt()
        bool1[i][j]=bool(a%2)
        bool2[i][j]=bool(a%3>=1)
# 创建点积数组
c=stdarray.create2D(n,n,0.0)
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]=c[i][j] or (bool1[i][k] and bool2[k][j])
# input
for row in c:
    for element in row:
        stdio.write(str(element)+'\t')
    stdio.writeln()
