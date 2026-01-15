for i in range(1, 21): # 满足公鸡数
    for j in range(1, 34): # 满足母鸡数
        for k in range(3, 301, 3): # 满足小鸡数
            if i + j + k == 100 and i * 5 + j * 3 + k / 3 == 100:
                print(i, j, k)

