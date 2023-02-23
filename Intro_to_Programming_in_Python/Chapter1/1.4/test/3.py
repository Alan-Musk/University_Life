import stdio
import sys
import random
import stdarray

index=11
array=stdarray.create1D(index,0.0)
for i in range(index):
    array[i]=i+1.0
    stdio.write(str(array[i])+' ')
stdio.writeln()
for i in range(index//2):
    temp=array[i]
    array[i]=array[index-1-i]
    array[index-1-i]=temp

for i in range(index):
    stdio.write(str(array[i])+' ')
stdio.writeln()
