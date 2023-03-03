import stdio

def signum(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    else:
        return '+1'

stdio.writeln(signum(0))