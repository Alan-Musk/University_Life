import stdarray
import stdio

def _flow(isOpen,isFull,i,j):
    n=len(isFull)
    if (i<0) or (i>=n):return
    if (j<0) or (j>=n):return
    if not isOpen[i][j]:return
    if isFull[i][j]:return

    isFull[i][j]=True
    _flow(isOpen,isFull,i+1,j)
    _flow(isOpen,isFull,i,j+1)
    _flow(isOpen,isFull,i,j-1)
    _flow(isOpen,isFull,i-1,j)

# 返回一个二维矩阵,表示全连通网格
def flow(isOpen):
    n=len(isOpen)
    isFull=stdarray.create2D(n,n,False)
    for j in range(n):
        _flow(isOpen,isFull,0,j)
    return isFull

# 检查返回结果矩阵的底部行,以确定系统是否可渗透
def percolates(isOpen):
    isFull=flow(isOpen)
    n=len(isFull)
    for j in range(n):
        if isFull[n-1][j]:return True
    return False

def main():
    isOpen=stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

if __name__== '__main__':main()