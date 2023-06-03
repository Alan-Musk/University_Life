# 请编写一个程序,实现下列功能:程序带两个正整数作为命令行参数,如果任意一个可以整除另一个数,则输出True
import stdio
import sys

if len(sys.argv) != 3:
    stdio.write("参数有误")
    sys.exit(1)

number1=int(sys.argv[1])
number2=int(sys.argv[2])

if number1 % number2 ==0 or number2 % number1 ==0:
    stdio.writeln("True")
else:
    stdio.writeln("False")