# 随机漫步艺术

import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

for _ in range(1000):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)
    t.forward(random.randint(10, 50))
    angle = random.choice([0, 90, 180, 270])
    t.right(angle)

turtle.done()