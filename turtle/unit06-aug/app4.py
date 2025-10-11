# 简谐运动图像（正弦波）

import turtle
import math

def draw_sine_wave():
    # 设置画布
    screen = turtle.Screen()
    screen.title("简谐运动图像")
    screen.setup(800, 400)
    
    # 创建海龟
    wave = turtle.Turtle()
    wave.speed(0)
    wave.penup()
    
    # 绘制坐标轴
    wave.goto(-350, 0)
    wave.pendown()
    wave.goto(350, 0)
    wave.penup()
    wave.goto(0, -150)
    wave.pendown()
    wave.goto(0, 150)
    wave.penup()
    
    # 绘制正弦波
    wave.goto(-350, 0)
    wave.pendown()
    wave.color("blue")
    
    for x in range(-350, 350):
        y = 100 * math.sin((x / 100) * 2 * math.pi)
        wave.goto(x, y)
    
    wave.penup()
    wave.hideturtle()
    turtle.done()

draw_sine_wave()