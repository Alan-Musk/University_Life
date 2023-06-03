import sys
import stddraw
import stdstats
from linkedqueue import Queue
from randomqueue import RandomQueue

# m:服务器的数量 n:项目任务的数量 t:采样大小 servers:队列
# best:采样中的最短队列 lengths:队列长度
m=int(sys.argv[1])
n=int(sys.argv[2])
t=int(sys.argv[3])

servers=RandomQueue()
for i in range(m):
    servers.enqueue(Queue())
for j in range(n):
    best=servers.sample()
    for k in range(1,t):
        queue=servers.sample()
        if len(queue)<len(best):
            best=queue
    best.enqueue(j)

lengths=[]
while not servers.isEmpty():
    lengths+=[len(servers.dequeue())]
stddraw.setYscale(0,2.0*n/m)
stdstats.plotBars(lengths)
stddraw.show()