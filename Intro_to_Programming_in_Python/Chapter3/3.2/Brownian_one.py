import sys
import stddraw
import stdrandom
from turtle import Turtle

trails=int(sys.argv[1])
step=float(sys.argv[2])
stddraw.setPenColor(stddraw.DARK_BLUE)
stddraw.setCanvasSize(800,800)
stddraw.setXscale(-10.0,12.0)
stddraw.setYscale(-10.0,12.0)
stddraw.setPenRadius(0.0)
turtle=Turtle(.5,.5,.0)
for t in range(trails):
    angle=stdrandom.uniformFloat(0.0,360.0)
    turtle.turnLeft(angle)
    turtle.goForward(step)
stddraw.show()