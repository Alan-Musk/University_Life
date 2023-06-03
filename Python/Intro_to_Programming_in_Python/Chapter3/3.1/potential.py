import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture

n=stdio.readInt()
charges=stdarray.create1D(n)
# 随机数存入电子数组
for i in range(n):
    x0=stdio.readFloat()
    y0=stdio.readFloat()
    q0=stdio.readFloat()
    charges[i]=Charge(x0,y0,q0)
# 设置一个最大宽度最大长度的空白图像
pic=Picture()
# 遍历整张图的像素
stdio.writeln(pic.width())
for col in range(pic.width()):
    for row in range(pic.height()):
        # 由于电子的坐标为0-1之间,将x,y的值转为0-1之间
        x=1.0*col/pic.width()
        y=1.0*row/pic.height()
        v=0.0
        for i in range(n):
            v+=charges[i].potentialAt(x,y)
        # 适当缩放保证在0-255以内
        v=(255/2.0)+(v/2.0e10)
        if v<0: gray=0
        elif v>255:gray=255
        else:gray=int(v)
        color=Color(gray,gray,gray)
        pic.set(col,pic.height()-1-row,color)
    stddraw.picture(pic)
    stddraw.show(10)

stddraw.show()


