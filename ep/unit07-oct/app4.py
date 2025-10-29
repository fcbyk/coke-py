"""
第四题，时间加上时间
"""

# 接收输入
h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

# 对应时间相加
h = h1 + h2
m = m1 + m2
s = s1 + s2

# 处理超出部分
m = m + s//60
h = h + m//60
s = s % 60
m = m % 60
h = h%24

# 输出结果
print(h, m, s, sep=":")