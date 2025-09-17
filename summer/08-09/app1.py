# 初始化
import turtle,random
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# 画图
for i in range(720):
    t.pencolor(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
    )
    t.pensize(i/100 + 1)
    t.forward(i)
    t.left(120)

# 结束绘图
turtle.done()