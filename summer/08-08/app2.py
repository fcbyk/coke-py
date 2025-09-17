import turtle
t = turtle.Turtle()

# 设置颜色模式
turtle.colormode(255)
t.color(0,240,255)

# 画点
# t.dot(100)

# 输入文字
t.penup()
t.write("hello",font=("黑体",20,"normal"))

# 结束绘图
turtle.done()