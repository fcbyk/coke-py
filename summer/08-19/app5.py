# 接收用户输入
heads = int(input("头的数量："))
feet = int(input("脚的数量："))

# 计算
r = (feet-2*heads)//2
c = heads-r

# 什么情况有解
a1 = (r >= 0)
a2 = (c >= 0)
a3 = (r*4+c*2 == feet)
a4 = (feet%2 == 0)

# 输出结果
if a1 and a2 and a3 and a4:
    print("鸡的数量：",c)
    print("兔的数量：",r)
else:
    print("无解")