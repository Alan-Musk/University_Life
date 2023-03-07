import sys
import stdio
from color import Color

def luminnance(c):
    red=c.getRed()
    green=c.getGreen()
    blue=c.getBlue()
    return red*.299+green*.587+blue*.114

def toGray(c):
    y=int(round(luminnance(c)))
    return Color(y,y,y)

def areCompatible(c1,c2):
    return abs(luminnance(c1)-luminnance(c2)) >= 128.0

def main():
    r1=int(sys.argv[1])
    g1=int(sys.argv[2])
    b1=int(sys.argv[3])
    r2=int(sys.argv[4])
    g2=int(sys.argv[5])
    b2=int(sys.argv[6])
    c1=Color(r1,g1,b1)
    c2=Color(r2,g2,b2)
    stdio.writeln(areCompatible(c1,c2))

if __name__=='__main__':main()

    