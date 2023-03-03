import stdio

def duplicate(s):
        t=s+s
        return t

s='Hello'
s=duplicate(s)
t='Bye'
t=duplicate(duplicate(duplicate(t)))
stdio.writeln(s+t)