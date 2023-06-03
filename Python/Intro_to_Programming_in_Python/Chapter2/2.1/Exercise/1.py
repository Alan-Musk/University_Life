import sys
import stdio

def max(num1,num2,num3):
    max=num1
    if max<num2:
        max=num2
    if max<num3:
        max=num3
    return max
    
num1=stdio.readFloat()
num2=stdio.readFloat()
num3=stdio.readFloat()
stdio.writeln('The largest one is '+str(max(num1,num2,num3)))