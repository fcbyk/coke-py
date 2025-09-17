# 旋转方块

import turtle

# 设置画布
screen = turtle.Screen()
screen.bgcolor("black")

# 创建海龟
square = turtle.Turtle()
square.speed(0)

# 绘制旋转方块
for i in range(72):
    # 改变颜色
    if i % 6 == 0:
        square.color("red")
    elif i % 6 == 1:
        square.color("orange")
    elif i % 6 == 2:
        square.color("yellow")
    elif i % 6 == 3:
        square.color("green")
    elif i % 6 == 4:
        square.color("blue")
    else:
        square.color("purple")
    
    # 绘制一个方块
    for _ in range(4):
        square.forward(100)
        square.right(90)
    
    # 旋转5度
    square.right(5)

turtle.done()
