# 导入海归库，创建画笔
import turtle
t = turtle.Turtle()

# 初始方向
t.left(30)

def dbx(a):
    for i in range(a):
        t.fd(80)
        t.left(360/a)

for a in range(3):
    dbx(3)
    t.left(120)

# 结束绘图
turtle.done()