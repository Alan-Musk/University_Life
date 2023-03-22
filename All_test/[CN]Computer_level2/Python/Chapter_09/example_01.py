import time

def coreLoop():
    limit=10**7
    while(limit>0):
        limit-=1
    
def otherLoop1():
    time.sleep(0.2)

def otherLoop2():
    time.sleep(0.4)

def main():
    startTime=time.localtime()
    print("程序开始时间",time.strftime('%Y-%m-%d %H:%M:%S',startTime))
    startPerfCounter=time.perf_counter()
    otherLoop1()
    otherLoop1PerfCounter=time.perf_counter()
    otherLoop1Perf=otherLoop1PerfCounter-startPerfCounter
    coreLoop()
    coreLoopPerfCounter=time.perf_counter()
    coreLoopPerf=coreLoopPerfCounter-otherLoop1PerfCounter
    otherLoop2()
    otherLoop2PerCounter=time.perf_counter()
    otherLoop2Perf=otherLoop2PerCounter-coreLoopPerfCounter
    endPerfCounter=time.perf_counter()
    totalPerf=endPerfCounter-startPerfCounter
    endTime=time.localtime()
    print("模块1运行时间是:{}秒".format(otherLoop1Perf))
    print("核心模块运行时间是:{}秒".format(coreLoopPerfCounter))
    print("模块2运行时间是:{}秒".format(otherLoop2Perf))
    print("程序运行总时间是:{}秒".format(totalPerf))
    print('程序结束时间:',time.strftime('%Y-%m-%d %H:%M:%S',endTime))
main()

