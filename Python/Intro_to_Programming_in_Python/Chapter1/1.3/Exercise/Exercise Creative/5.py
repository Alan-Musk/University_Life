import sys

def find_median(a, b, c, d, e):
    if d>e:
        d,e=e,d
    if b>c:
        b,c=c,b
    if c>e:
        c,e=e,c
    if a>d:
        a,d=d,a
    if c>d:
        c,d=d,c
    if a>c:
        a,c=c,a
    return c

if len(sys.argv) != 6:
    print("Usage: python median.py a b c d e")
else:
    a, b, c, d, e = [int(arg) for arg in sys.argv[1:]]
    median = find_median(a, b, c, d, e)
    print("The median value is:", median)
