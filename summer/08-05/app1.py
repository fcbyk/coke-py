# 导入海龟库
import turtle

# 创建画笔
t = turtle.Turtle()

# 画风车
t.left(90)
# 画第一个三角形
for i in range(3):
    t.forward(100)
    t.right(120)

# 改变初始方向，转120度
t.right(120)

# 画第二个三角形
for i in range(3):
    t.forward(100)
    t.right(120)

# 转120度
t.right(120)

# 隐藏画笔，结束绘图
t.hideturtle()
turtle.done()