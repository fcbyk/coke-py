# 初始化
import turtle
t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)

# 画海报的背景
t.fillcolor(10,200,255)
t.penup()
t.goto(-150,200)
t.pendown()
t.begin_fill()
# 这里画矩形(300x400)
t.fd(300)
t.right(90)
t.fd(400)
t.right(90)
t.fd(300)
t.right(90)
t.fd(400)
t.right(90)
t.end_fill()

# 标题
t.penup()
t.goto(-110,100)
t.write("欢度国庆·演讲大赛",font=("楷体",18,"bold"))


# 结束绘图
turtle.done()