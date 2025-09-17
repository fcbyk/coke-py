# 输入一个数字，判断它是奇数还是偶数

for i in range(100):
    num = int(input("请输入一个数字："))

    if num%2 == 0:
        print("偶数")
    else:
        print("奇数")