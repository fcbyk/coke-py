"""
第四题：位数分离
"""

# 接收输入
num = int(input("请输入一个三位整数："))

# 计算结果
ge = num%10
shi = num//10%10
bai = num//100

# 输出结果
print(ge,shi,bai)
