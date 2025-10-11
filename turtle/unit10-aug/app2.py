# 初始化
import turtle
t = turtle.Turtle()
t.speed(0)
t.pencolor("green")

# 画图
for i in range(100):
    t.circle(i)
    t.rt(12)

# 结束绘图
t.ht()
turtle.done()