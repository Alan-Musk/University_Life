import stdio
import stdarray

n=3
m=10
right=[0.25,0.25,0.5]
grades=stdarray.create2D(m,n,0.0)
for i in range(m):
    for j in range(n):
        grade=stdio.readInt()
        grades[i][j]=grade
nums=stdarray.create1D(m,0.0)
for i in range(m):
    for j in range(n):
        nums[i]+=grades[i][j]*right[j]
for num in range(m):
    stdio.write(grades[num])
    stdio.write("   ")
    stdio.writeln(nums[num])
