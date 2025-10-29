"""
第二题，秒转换成时间
"""
n = int(input())
h = n // 3600
m = n % 3600 // 60
s = n % 60
print(h, m, s, sep=":")
