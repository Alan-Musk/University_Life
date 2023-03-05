import sys
import stdio

def moves(n,left):
    if n==0: return 
    moves(n-1,not left)
    if left:
        stdio.writeln(str(n)+'  left')
    else:
        stdio.writeln(str(n)+'  right')
    moves(n-1,not left)

n=int(sys.argv[1])
moves(n,True)