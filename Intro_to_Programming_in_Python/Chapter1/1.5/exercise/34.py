import stdio
import sys
import random
import stdarray
import stddraw

stddraw.setXscale(-1.0,1.0)
stddraw.setYscale(-1.0,1.0)

DT=100
RADIUS=0.05
rx=0.480
ry=0.860
vx=0.015
vy=0.023


stddraw.clear(stddraw.GRAY)
while True:
    if abs(rx+vx)+RADIUS > 1.0:vx=-vx
    if abs(ry+vy)+RADIUS > 1.0:vy=-vy
    rx=rx+vx
    ry=ry+vy
#     stddraw.show(DT)
#     stddraw.setPenColor(stddraw.WHITE)
#     stddraw.filledCircle(rx,ry,RADIUS)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledCircle(rx,ry,RADIUS)
    # stddraw.show(DT)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.circle(rx,ry,RADIUS)
    stddraw.show(DT)


