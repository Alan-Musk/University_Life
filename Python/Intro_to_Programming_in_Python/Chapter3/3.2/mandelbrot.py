import sys
import stddraw
from color import Color
from picture import Picture

# return 灰度
def mandel(z0,limit):
    z=z0
    for i in range(limit):
        if abs(z)>2.0:  return i
        z=z*z+z0
    return limit
n=int(sys.argv[1]) # n*n像素图像
xc=float(sys.argv[2])   # 图像中心点
yc=float(sys.argv[3])   # 图像中心点
size=float(sys.argv[4]) # 图像大小
# 创建图像对象
pic=Picture(n,n)
# 遍历图像
for col in range(n):
    for row in range(n):
        x0=xc-size/2+size*col/n
        y0=yc-size/2+size*row/n
        z0=complex(x0,y0)
        gray=255-mandel(z0,255)
        color=Color(gray,gray,gray)
        pic.set(col,n-1-row,color)
stddraw.setCanvasSize(n,n)
stddraw.picture(pic)
stddraw.show()