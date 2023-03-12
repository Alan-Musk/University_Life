import sys
import stddraw
import stdrandom
from linkedqueue import Queue
from histogram import Histogram
# lambd:到达速率 mu:服务速率 histogram:直方图 queue:MM1队列
# nextArrival:下一个到达的时间 nextService:下一个服务完成的时间
# arrival:下一个客户服务的到达时间 wait:队列中的时间
lambd=float(sys.argv[1])
mu=float(sys.argv[2])

histogram=Histogram(60+1)
queue=Queue()
stddraw.setCanvasSize(700,500)

nextArrival=stdrandom.exp(lambd)
nextService=nextArrival+stdrandom.exp(mu)

while True:
    while nextArrival<nextService:
        queue.enqueue(nextArrival)
        nextArrival+=stdrandom.exp(lambd)
    arrival=queue.dequeue()
    wait=nextService-arrival
    stddraw.clear()
    histogram.addDataPoint(min(60,int(round(wait))))
    histogram.draw()
    stddraw.show(20.0)
    if queue.isEmpty():
        nextService=nextArrival+stdrandom.exp(mu)
    else:
        nextService=nextService+stdrandom.exp(mu)