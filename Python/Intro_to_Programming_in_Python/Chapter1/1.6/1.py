import stdarray
import stdio

n=stdio.readInt()

linkCounts=stdarray.create2D(n,n,0) #从页面i到页面j的超链接数量
outDegrees=stdarray.create1D(n,0)   #页面i包含的超链接数量转换概率

times=1
while not stdio.isEmpty():
    # 积累链接数量
    i=stdio.readInt()
    j=stdio.readInt()
    outDegrees[i]+=1
    linkCounts[i][j]+=1
    

stdio.writeln(str(n))

for i in range(n):
    for j in range(n):
        p=(0.9*linkCounts[i][j]/outDegrees[i])+(0.10/n)
        stdio.writef('%8.5f',p)
    stdio.writeln()
