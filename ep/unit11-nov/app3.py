def mySum(n):
    ge = n % 10
    shi = n // 10 % 10
    bai = n // 100
    # print(ge + shi + bai)
    return ge + shi + bai


n = int(input())
a = mySum(n)
print(a)

