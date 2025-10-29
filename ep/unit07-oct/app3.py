"""
第三题，时间加上秒数
"""
h = int(input())
m = int(input())
s = int(input())
t = int(input())

s = s + t
m = m + s//60
h = h + m//60
s = s % 60
m = m % 60
print(h, m, s, sep=":")
