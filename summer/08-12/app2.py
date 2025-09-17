# 初始化
import turtle,random
t = turtle.Turtle()
t.speed(0)
t.pensize(10)

turtle.colormode(255)

# 画第一个线
for i in range(20):
    t.pencolor(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )
    t.penup()
    t.goto(0,0)
    t.fd(80)
    t.pendown()
    t.fd(25)
    t.left(18)


# 结束绘图
turtle.done()