import stdio
import sys
import random
import stdarray

n=int(sys.argv[1])
trials=int(sys.argv[2])
deadEnds=0
for t in range(trials):
    a=stdarray.create2D(n,n,False)
    x=n//2
    y=n//2
    # 在找出口,走过的都是True
    while (x>0) and (x<n-1) and (y>0) and (y<n-1):
        a[x][y]=True
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            deadEnds+=1
            break
        r=random.randrange(1,5)
        if (r==1) and (not a[x+1][y]):x+=1
        elif (r==2) and (not a[x-1][y]):x-=1
        elif (r==3) and (not a[x][y+1]):y+=1
        elif (r==4) and (not a[x][y-1]):y-=1

stdio.writeln(str(100*deadEnds//trials)+'% dead ends')
