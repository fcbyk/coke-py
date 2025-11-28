arr = [100,200,300,11]

# 列表的索引
print(arr[0])
print(arr[-1])

# 用sum函数 求和
print(sum(arr))

# 增删改查
arr.append(200) #尾部添加元素
arr.remove(11)  # 删除指定元素
arr.index(300)  # 查找元素编号
arr[1] = 10086  # 修改

print(arr)

