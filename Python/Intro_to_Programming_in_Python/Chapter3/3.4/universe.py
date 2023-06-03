import sys
import stdarray
import stddraw
from body import Body
from instream import InStream
from vector import Vector

class Universe:
    # 构造函数 n:天体数量 radius:半径
    def __init__(self,filename) -> None:
        instream=InStream(filename)
        n=instream.readInt()
        radius=instream.readFloat()
        # 设置画布大小
        stddraw.setXscale(-radius,radius)
        stddraw.setYscale(-radius,radius)
        # 创造天体
        self._bodies=stdarray.create1D(n)
        for i in range(n):
            rx=instream.readFloat()
            ry=instream.readFloat()
            vx=instream.readFloat()
            vy=instream.readFloat()
            mass=instream.readFloat()
            r=Vector([rx,ry])
            v=Vector([vx,vy])
            self._bodies[i]=Body(r,v,mass)
    # 通过模拟天体dt秒来更新宇宙
    def increaseTime(self,dt):
        n=len(self._bodies)
        f=stdarray.create1D(n,Vector([0,0]))
        # 遍历天体,逐个作用,将作用力总和存入f数组中
        for i in range(n):
            for j in range(n):
                if i !=j:
                    bodyi=self._bodies[i]
                    bodyj=self._bodies[j]
                    f[i]=f[i]+bodyi.forceFrom(bodyj)
        for i in range(n):
            self._bodies[i].move(f[i],dt)
    
    def draw(self):
        for body in self._bodies:
            body.draw()

def main():
    universe=Universe(sys.argv[1])
    dt=float(sys.argv[2])
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(5)

if __name__=='__main__':main()