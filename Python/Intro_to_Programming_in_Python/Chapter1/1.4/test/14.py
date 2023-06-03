# Compose a program that accepts an integer n from the command line and creates an n-by-n boolean array a such that a[r][c] is True if r and c are relatively prime (have no common factors other than 1), and False otherwise. Then write the array (see a previous exercise in this section of the booksite) using * to represent True and a space to represent False. Include row and column numbers. Hint: Use sieving.
import stdio
import sys
import stdarray

# 使用函数检查两个数是互素
def is_relatively_prime(x,y):
    for i in range(2,min(x,y)+1):
        if x%i==0 and y%i==0:
            return False
    return True
# 从命令行获取n
n=int(sys.argv[1])
# 创建数组
boolArray=stdarray.create2D(n,n,False)
for i in range(n):
    for j in range(n):
        if is_relatively_prime(i+1,j+1):
            boolArray[i][j]=True

# 显示数组
print('   ', end='')
for j in range(n):
    print(str(j+1).ljust(2), end=' ')
print()
print('---' + '--'*n)
for i in range(n):
    print(str(i+1).ljust(2) + '|', end=' ')
    for j in range(n):
        if boolArray[i][j]:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 输出


