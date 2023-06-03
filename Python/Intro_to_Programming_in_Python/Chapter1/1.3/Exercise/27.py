import stdio
import sys

n=int(sys.argv[1])

for num in range(n):
    for j in range(n):
        if num%2==0:
            stdio.write('* ')
        else:
            stdio.write(' *')
    stdio.writeln('')