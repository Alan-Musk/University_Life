import stdio
import sys

sum=int(sys.argv[1])
i=0
while i<=sum:
    if(i%10==1):
        stdio.writeln(str(i)+'st Hello')
    elif (i%10==2):
        stdio.writeln(str(i)+'nd Hello')
    elif (i%10==3):
        stdio.writeln(str(i)+'rd Hello')
    else:
        stdio.writeln(str(i)+'th Hello')
    i+=1