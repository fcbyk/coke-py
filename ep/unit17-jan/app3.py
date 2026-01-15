# 接收输入, 字符串，每个元素以空格隔开
a = input()
# 以空格为分割符, 转成字符列表
b = a.split()
# 字符列表 -> 整型列表
c = list(map(int,b))

for i in b:
    print(i)