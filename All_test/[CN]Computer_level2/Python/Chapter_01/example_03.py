from turtle import *

# 设置颜色并开启填充模式
color('red', 'pink')
begin_fill()

# 绘制五角星
for i in range(5):
    fd(200)
    rt(144)

# 关闭填充模式
end_fill()

# 隐藏画笔并保持窗口打开
hideturtle()
done()
