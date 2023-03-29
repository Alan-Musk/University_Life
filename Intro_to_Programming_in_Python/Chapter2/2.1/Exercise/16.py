import stdarray
import stdrandom

def histogram(a,m):
    num=stdarray.create1D(m)

m=50
a=stdarray.create1D(100)
for i in a:
    i=stdrandom.random(0,m-1)
print(a)