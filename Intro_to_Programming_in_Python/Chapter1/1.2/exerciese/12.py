#请编写一个程序,实现下列功能:程序带三个正整数作为命令行参数,如果其中任意一个数大于或等于两个数之和,则输出False,否则输出True.
# 该程序可用于测试三个数是否满足构成三角形三条边的条件
import stdio
import sys

if len(sys.argv)!=4:
    stdio.writeln("参数有误")
    sys.exit()

num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])

if num1>=(num2+num3) or num2>=(num1+num3) or num3>=(num1+num2):
    stdio.writeln("True")
else:
    stdio.writeln("False")