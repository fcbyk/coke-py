# 初始化
import turtle
t = turtle.Turtle()
t.pensize(10)
t.left(90)
t.color('lightblue')

# 画信号条
for i in range(20,101,20):
    t.penup()
    t.goto(i-100,0)
    t.pendown()
    t.fd(i)

# 结束绘图
t.ht()
turtle.done()