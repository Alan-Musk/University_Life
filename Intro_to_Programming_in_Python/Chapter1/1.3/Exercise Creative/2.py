import stdio
import sys
import math

number=int(sys.argv[1])
string=''
sum_all=0
x=0
for k in range (2,11):
    
    x=number%10
    string=str(x)+string
    sum_all+=x*k
    number=number//10
x=11-(sum_all%11)
if x>9:
    string=string+'X'
else:
    string=string+str(x)
stdio.writeln(string)
