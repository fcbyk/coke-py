'''
range生成一个序列
range(开始，结束，步长)
'''

# 一个参数  [0,1,2]
r1 = range(3)

# 两个参数  [2,3,4]
r2 = range(2,5)

# 三个参数  [2,4,6,8]
r3 = range(2,10,2)


# 使用list函数，把生成的序列转成列表
print(list(r1))

# 使用for循环把序列的数字，一个个取出来
for i in r3:
    print(i)

# for循环把列表元素一个个取出来
for i in ["张三","李四",100,200]:
    print(i)