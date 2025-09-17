# 导入海归库，创建画笔
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(5)

# 彩色贝壳
r = 160
cl = ["blue","red","pink","yellow","green"]
for i in cl:
    t.pencolor(i)
    t.circle(r)
    r = r - 20


# 结束绘图
turtle.done()