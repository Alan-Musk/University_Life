import math
import sys
import stddraw
import stdrandom

def curve(x0,y0,x1,y1,var,beta,n=7):
    if n==0:
        stddraw.line(x0,y0,x1,y1)
        return 
    xm=(x0+x1)/2.0
    ym=(y0+y1)/2.0
    delta=stdrandom.gaussian(0.0,math.sqrt(var))
    curve(x0,y0,xm,ym+delta,var/beta,beta,n-1)
    stddraw.show(500)
    curve(xm,ym+delta,x1,y1,var/beta,beta,n-1)

hurstExponent=float(sys.argv[1])
stddraw.setPenRadius(0.0)
beta=2.0**(2.0*hurstExponent)
curve(0.0,0.5,1.0,0.5,0.01,beta)
stddraw.show()
