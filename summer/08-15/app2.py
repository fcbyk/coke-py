# 初始化
import turtle
t = turtle.Turtle()
t.speed(0)

# 定义二个函数
def mygoto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# 定义画矩形函数
def zfx(w,h,color):
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

# 调用函数
zfx(50,100,"yellow")

# 结束绘图
turtle.done()