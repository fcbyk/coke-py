# 接收输入
nums = list(map(int,input().split()))

# 使用一个保存最小值
min = nums[0]
for i in nums:
    # 如果比最小值小，则更新变量
    if i < min:
        min = i

# 输出结果
print(min)