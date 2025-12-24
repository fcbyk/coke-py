# 接收输入
math = float(input("请输入数学成绩："))
english = float(input("请输入英语成绩："))

# 英语80分以上 并且(与) 数学80分以上
if english >= 80 and math >= 80:
    print("奖励吃KFC一次")

# 英语满分 或者(或) 数学满分
if english >= 100 or math >= 100:
    print("奖励吃KFC一次")

# 有一科不及格，挨批
if english < 60 or math < 60:
    print("挨批")