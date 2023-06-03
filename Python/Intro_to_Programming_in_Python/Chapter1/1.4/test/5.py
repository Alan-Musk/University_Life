import stdio
import sys
import random
import stdarray

index=10
array=stdarray.create2D(index,index,False)

for i in range(index):
    j=1
    while j<index:
        array[i][j]=True
        j+=2

stdio.write('   ')
for i in range(index):
    stdio.write('  '+str(i))
stdio.writeln()
for i in range(index):
    stdio.write(i)
    for j in range(index):
        if array[i][j]:
            stdio.write(' * ')
        else:
            stdio.write('   ')
    stdio.writeln()