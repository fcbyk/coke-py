"""
第一题：数值交换
"""

# 接收输入
a = int(input())
b = int(input())

# 交换两个变量的值（使用临时变量）
temp = a
a = b
b = temp

# 输出结果
print(a,b)

# 交换两个变量的值（使用元组解包）
a,b = b,a

# 输出结果
print(a,b)



