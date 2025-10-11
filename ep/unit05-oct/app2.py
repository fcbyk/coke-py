"""
第二题：物品交换
"""

# 接收用户输入
lele = input()
meimei = input()
mingming = input()

# 乐乐和美美交换
temp = lele
lele = meimei
meimei = temp

# 乐乐和明明交换
temp = mingming
mingming = lele
lele = temp

# 输出结果
print(lele, meimei, mingming,sep="\n")