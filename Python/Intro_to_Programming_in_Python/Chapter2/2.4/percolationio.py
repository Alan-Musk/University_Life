import sys
import stdarray
import stdio
import stddraw
import stdrandom

# 生成n*n的bool数组,通过stdrandom中的函数,将0-1中小于p的为true
def random(n,p):
    a=stdarray.create2D(n,n,False)
    for i in range(n):
        for j in range(n):
            a[i][j]=stdrandom.bernoulli(p)
    return a

# 逐一判断数组元素,如果是which则为方块
def draw(a,which):
    n=len(a)
    stddraw.setXscale(-1,n)
    stddraw.setYscale(-1,n)
    for i in range(n):
        for j in range(n):
            if a[i][j]==which:
                stddraw.filledSquare(j,n-i-1,0.55)

def main():
    n=int(sys.argv[1])
    p=float(sys.argv[2])
    test=random(n,p)
    draw(test,False)
    stddraw.show()

if __name__== '__main__':main()