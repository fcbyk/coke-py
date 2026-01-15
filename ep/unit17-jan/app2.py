# range函数
# 这个函数可以生成序列

# 生成0-10
a = range(11)
# 转成列表并打印
ls = list(a)
print(ls)

# 两个参数 (开始，结束+1)
ls = list(range(10,56))
print(ls)

# 三个参数 (开始，结束+1，步长)
# 0 到 20 的所有偶数
ls = list(range(0,21,2))
print(ls)

# 生成序列，0-50所有奇数
# 0-100，5的倍数