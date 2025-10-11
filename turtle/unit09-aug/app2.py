# 初始化
import turtle,random
t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.pensize(5)
t.seth(45)

for i in range(5):
    t.penup()
    
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.goto(x,y)

    t.pendown()
    t.circle(50,steps=4)

# 结束绘图
turtle.done()