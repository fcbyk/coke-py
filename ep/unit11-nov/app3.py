def wSum(num):
    ge = num%10     # 求个位
    shi = num//10%10    # 求十位
    bai = num//100      # 求百位
    sum = ge + shi + bai    # 位数之和
    return sum         # 返回值

print( wSum(123) )
print( wSum(111) + wSum(222) )

def f(x):
    return x * x


print( f(100) + f(10) )