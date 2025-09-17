# 初始化
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# 定义一个函数
def myCircle(x,y,cl,r):
    t.color(cl)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)

# 调用函数
myCircle(-105,50,"blue",23)
myCircle(-50,50,"black",23)
myCircle(5,50,"red",23)
myCircle(-78,20,"orange",23)
myCircle(-23,20,"green",23)

t.ht()
turtle.done()