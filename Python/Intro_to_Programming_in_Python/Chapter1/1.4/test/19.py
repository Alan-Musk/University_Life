import stdarray
import sys
import stdio

n=int(sys.argv[1])
array=stdarray.create2D(n,n,False)
a=stdarray.create1D(n,array)
stdio.writeln(a)
