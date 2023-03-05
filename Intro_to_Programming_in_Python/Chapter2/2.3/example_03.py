import sys
import stdio

def moves(n,enter):
    if n==0:return 
    moves(n-1,True)
    if enter:
        stdio.writeln('enter '+str(n))
    else:
        stdio.writeln('exit '+str(n))
    moves(n-1,False)

n=int(sys.argv[1])
moves(n,True)