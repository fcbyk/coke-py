for x in range(1,10):
    for y in range(10):
        for z in range(10):
            s1 = x * 100 + y * 10 + z
            s2 = x ** 3 + y ** 3 + z ** 3
            if s1 == s2:
                print(f'{s1}是水仙花数')

