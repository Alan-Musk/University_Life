import sys
import stdarray
import stddraw
import stdrandom
from turtle import Turtle
from color import Color

# 传入基本参数
n=int(sys.argv[1])  # 多少只海龟
trials=int(sys.argv[2]) # 每只运动多少次
step=float(sys.argv[3]) # 每次运动的距离
# 画板设置
stddraw.setCanvasSize(800,800)
stddraw.setXscale(-10.0,10.0)
stddraw.setYscale(-10.0,10.0)
stddraw.setPenRadius() 
# 创建海龟对象数组,海龟颜色数组 
turtles=stdarray.create1D(n)
color=stdarray.create1D(n)
# 给颜色数组赋值
for i in range(n):
    r=stdrandom.uniformInt(0,255)
    g=stdrandom.uniformInt(0,255)
    b=stdrandom.uniformInt(0,255)
    color[i]=Color(r,g,b)

# 往数组中放入海龟对象
for i in range(n):
    x=stdrandom.uniformFloat(-5.0,5.0)
    y=stdrandom.uniformFloat(-5.0,5.0)
    turtles[i]=Turtle(x,y,0.0)
# 运动开始!
for t in range(trials):
    # 每只运动一下
    for i in range(n):
        stddraw.setPenColor(color[i])
        angle=stdrandom.uniformFloat(0.0,360.0)
        turtles[i].turnLeft(angle)
        turtles[i].goForward(step)
stddraw.show()