import stddraw              # 导入画图模块
from vector import Vector   # 导入向量数据类型

class Body:
    # 构造函数 r:位置 V:速度 mass:质量
    def __init__(self,r,v,mass) -> None:
        self._r=r
        self._v=v
        self._mass=mass
    # 给self施加f的力,运动dt秒
    def move(self,f,dt):
        a=f.scale(1.0/self._mass) # a:加速度 a=f/m 
        self._v=self._v+a.scale(dt)
        self._r=self._r+self._v.scale(dt)
    # 计算self和other之间的引力
    def forceFrom(self,other):
        G=6.67e-11
        delta=other._r-self._r # 向量相减
        dist=abs(delta)         # 物体之间的距离
        m1=self._mass           # self的质量
        m2=other._mass          # other的质量
        magnitude=G*m1*m2/(dist*dist)  # 计算引力 
        return delta.direction().scale(magnitude) # 力向量方向跟两个物体位置向量差的方向相同 f是力的大小与方向的乘积
    # 画图
    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0],self._r[1])

