# 19的倍数

# for i in range(100, 1001):
#     if i % 19 == 0:
#         print(i)
#         break


# 前10个，19的倍数
cnt = 0
for i in range(100, 1001):
    if i % 19 == 0:
        print(i)
        cnt += 1
    if cnt == 10:
        break

# 不是19的倍数
for i in range(100, 1001):
    if i % 19 == 0:
        continue
    print(i)