import sys
import stdio

def search(front,later):
    if (later-front)==1:
        return front
    num=(front+later)//2
    stdio.write('Greater than or equal to '+str(num)+'?')
    if stdio.readBool():
        return search(num,later)
    else:
        return search(front,num)
k=int(sys.argv[1])
m=int(sys.argv[2])
n=m**k
stdio.write('Think of a number ')
stdio.writeln('between 0 and '+str(n-1))
guess=search(0,n-1)
stdio.writeln('Your number is '+str(guess))
