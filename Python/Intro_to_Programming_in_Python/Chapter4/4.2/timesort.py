# f():要测试的函数 n:问题规模的大小 trials:程序运行次数 total:总消耗的时间 a[]要排序的数组 watch:秒表
import stdio
import stdrandom
import stdarray
from stopwatch import Stopwatch
import insertion


def timeTrials(f,n,trials):
    total=0.0
    a=stdarray.create1D(n,0.0)
    for t in range(trials):
        for i in range(n):
            a[i]=stdrandom.uniformFloat(0.0,1.0)
        watch=Stopwatch()
        f(a)
        total+=watch.elapsedTime()
    return total
# n:问题规模的大小 prev:问题规模为n//2时的运行时间 curr:问题规模为n时的运行时间 ratio:运行时间的比值
def doublingTest(f,n,trails):
    while True:
        prev=timeTrials(f,n//2,trails)
        curr=timeTrials(f,n,trails)
        ratio=curr/prev
        stdio.writef('%7d %4.2f\n',n,ratio)
        n*=2

def main():
    doublingTest(insertion.sort,128,100)

if __name__=='__main__':main()