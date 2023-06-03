import sys
import stdio

# 求最大公约数的函数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(sys.argv[1])
for i in range(1, n+1):
    for j in range(1, n+1):
        if gcd(i, j) == 1:
            stdio.write(' * ')
        else:
            stdio.write('   ')
    stdio.writeln('')
