# 初始化
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# 新建变量
a = turtle.textinput("","几边形?")
b = turtle.textinput("","边长？")
c = turtle.textinput("","旋转几次？")

# 字符串转成数字
a = int(a)
b = int(b)
c = int(c)

# 画旋转多边形
for i in range(c):
    # 画多边形
    for i in range(a):
        t.fd(b)
        t.left(360/a)
    # 画完一个图形，改变初始方向
    t.lt(360/c)

# 结束绘图
turtle.done()