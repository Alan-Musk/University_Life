import stdio
import sys
import random
import stdarray
index=2
# a=stdarray.create2D(index,index,1.0)  #a
# a=stdarray.create2D(index,5,1.0)  #b
a=[[1,2,34,54,32,4,2],[24,24,22],[3,3,3,3,3,33,3,33,3,3,33,3,3]]   #c
n=len(a)    #获取a的外部长度
#获取a的内部长度
insides=[]
for i in range(n):
    insides+=[len(a[i])]
    
b=[]
# 创建b数组
for i in range(n):
    b+=[[0 for i in range(insides[i])]]
    for k in range(insides[i]):
        b[i][k]=a[i][k]
        

stdio.writeln(b)

