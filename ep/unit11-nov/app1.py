# 函数定义
def tree():
    # 选中按 TAB键 缩进
    # 选中按 shift  +  TAB键 反缩进
    print("      *")
    print("     ***")
    print("    *****")
    print("   *******")
    print("  *********")
    print(" ***********")
    print("     ***")
    print("     ***")
    print("     ***")

# 函数调用
tree()
tree()
tree()


def hello(name="没有名字",age=0):    # 形式参数
    print("你好，我是", name)
    print("我今年", age, "岁")

hello("小明", 10) # 实际参数
hello("小红", 9)
hello(age=9, name="小江")
hello() # 使用默认参数




























# def hello(name,age):    # 形参
#     print("我是",name)
#     print("我的年龄是",age,"岁")
#
# hello("楚天",10)     # 实参
# hello("文韬",9)
# hello(age=100,name="苦力怕")