'''
函数就像一个魔法盒子，你给它一些东西（输入）
它就会按照自己的规则做一些事情，然后给你一个结果（输出）
'''

# 往控制台打印数据
print()

# 使用type查看数据的类型
type(100)

# 强制类型转化
int()
str()
float()

# 示例1
print(type(100))
print(type(10.0))
print(type("hello"))
print(type('hello'))

# 示例2
a = "100"
b = "200"
print(a+b)
c = int(a) + int(b)
print(c)