for i in range(60): # i 表示鸡的数量
    for j in range(60): # j 表示兔子的数量
        if 2 * i + 4 * j == 60: # 如果脚的数量刚好是60，就得出一组正确答案
            print(i, j) # 输出这一组答案
