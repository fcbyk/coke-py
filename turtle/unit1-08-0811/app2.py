# 导库
import random,turtle

t = turtle.Turtle()
turtle.colormode(255)

# 产生随机数
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

# # t.color(23,100,21)
t.color(r,g,b)

t.dot(100)

turtle.done()