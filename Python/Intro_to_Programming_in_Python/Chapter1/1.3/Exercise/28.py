import stdio
import sys

if len(sys.argv)!=3:
    stdio.writeln('参数错误')
    sys.exit(1)

num1=int(sys.argv[1])
num2=int(sys.argv[2])
temp=0
while True: 
    if num1>num2:
        if num1%num2==0:
            stdio.writeln('最大公约数是:'+str(num2))
            break
        else:
            num1=num1-num2
    else:
        temp=num1
        num1=num2
        num2=temp