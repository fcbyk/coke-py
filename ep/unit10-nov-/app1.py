arr = input()   # 接收输入
arr = arr.split()   # 字符串 -> 列表
print(arr)

arr = list(map(int,arr))  # 字符串列表 -> 整型列表
print(arr)
print(sum(arr))     # 求和