import sys
import stdio

def search(lo,hi):
    if(hi-lo)==1:
        return lo
    mid=(hi+lo)/2
    stdio.write('Greater than or equal to '+str(mid)+'?')
    if stdio.readBool():
        return search(mid,hi)
    else:
        return search(lo,mid)

k=int(sys.argv[1])
n=2**k
stdio.write('Think of a number ')
stdio.writeln('between 0 and '+str(n-1))
guess=search(0,n)
stdio.writeln('Your number is '+str(guess))