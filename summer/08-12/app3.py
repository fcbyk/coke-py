import turtle
t = turtle.Turtle()

# 接收用户输入
heads = int(  turtle.textinput("","头的数量？")  )
feet = int(  turtle.textinput("","脚的数量？")  )

# 计算
r = (feet-2*heads)//2
c = heads-r

t.penup()

# 输出结果
if True:
    t.write(
            "鸡的数量："+str(c),
            font=("黑体",20,"bold"))
    t.goto(0,-30)
    t.write(
            "兔的数量："+str(r),
            font=("黑体",20,"bold")
            )
else:
    t.write(
        "无解",
        font=("黑体",20,"bold"))

# 结束绘图
t.ht()
turtle.done()