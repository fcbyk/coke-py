# 初始化
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# 背景颜色
turtle.bgcolor("black")

# 初始方向，正数左转，负数右转
t.seth(45)

# 内接多边形
t.color("white")
# t.circle(100,steps=4)
# t.circle(-100,steps=3)

# 画弧线
t.circle(100,180)

# 结束绘图
turtle.done()