import sys
import stdio

def gcd(p,g):
    if g==0:return p
    return gcd(g,p%g)

def main():
    p=int(sys.argv[1])
    g=int(sys.argv[2])
    stdio.writeln(gcd(p,g))

if __name__ =='__main__':main()