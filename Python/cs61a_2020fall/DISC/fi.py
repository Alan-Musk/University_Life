def hailstone(n,g):
    if n==1:
        h=g
    elif n%2!=0:
        h=up
    else:
        h=down
    
    return h(n,g)

def up(n,f):
    return 1+f(3*n+1)

def down(n,f):
    return 1+f(n//2)

hailstone(10,print)
