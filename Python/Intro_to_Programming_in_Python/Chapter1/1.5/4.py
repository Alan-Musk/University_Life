import sys
import stdio

lo=int(sys.argv[1])
hi=int(sys.argv[2])

while not stdio.isEmpty():
    value=stdio.readInt
    if(value>=lo) and (value<=hi):
        stdio.write(str(value)+' ')
stdio.writeln()
