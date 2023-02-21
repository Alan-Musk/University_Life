import stdio
import sys

n=int(sys.argv[1])
for i in range(2,n+1):
    isPrime=1
    for k in range (2,i-1):
        if i%k==0:
            isPrime=0
        k+=1 
    if isPrime==1:
        stdio.write(str(i)+' ')
stdio.writeln('')
