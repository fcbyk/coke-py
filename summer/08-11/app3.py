# 初始化
import random,turtle
t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)

# 画图
for i in range(30):
    t.pencolor(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
    )
    t.circle(50)
    t.lt(360/30)

# 结束绘图
turtle.done()