import stdio
import math
from arraystack import Stack

ops=Stack()
values=Stack()

while not stdio.isEmpty():
    token=stdio.readString()
    if token=='+':ops.push(token)
    elif token=='-':ops.push(token)
    elif token=='*':ops.push(token)
    elif token=='sqrt':ops.push(token)
    elif token==')':
        op=ops.pop()
        value=values.pop()
        if op=='+':value=values.pop()+value
        elif op=='-':value=values.pop()-value
        elif op=='*':value=values.pop()*value
        elif op=='sqrt':value=math.sqrt(value)
        values.push(value)
    elif token!='(':
        values.push(float(token))
stdio.writeln(values.pop())
        