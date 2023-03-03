import stdio

def lg(n):
    w=0
    while n>2:
        n/=2
        w+=1
    return w

stdio.writeln(lg(10))