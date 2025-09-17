# 单行注释，可以按ctrl + /

'''
多行注释
使用3个单引号
'''

"""
多行注释
使用3个双引号
"""

# 导入工具箱
import turtle

# 创建画笔,命名为t
t = turtle.Turtle()
t = turtle.Pen()

# 改变形状
t.shape("turtle")

# 前进后退，左转右转
t.forward(100)
t.back(100)
t.left(90)
t.right(90)

# 前进后退，左转右转,简写形式
t.fd(100)
t.bk(100)
t.lt(90)
t.rt(90)

# 设置颜色
t.pencolor("blue")  # 设置画笔颜色
t.fillcolor("red")  # 设置填充颜色
t.color("pink")     # 同时设置画笔颜色和填充颜色
t.begin_fill()      # 开始填充
t.end_fill()        # 结束填充

# 隐藏和显示画笔
t.hideturtle()
t.showturtle()

# 隐藏和显示画笔-简写
t.ht()
t.st()

# 改变画笔粗细
t.pensize(5)
t.width(5)

# 画圆（空心圆、实心圆）
t.circle(100)
t.dot(100)

# 抬笔、落笔
t.penup()
t.pendown()
t.pd()
t.pu()
t.up()
t.down()

# 移动到某个坐标
t.goto(100,100)

# 画笔速度(0-10)
t.speed(0)

# 完成绘图
turtle.done()