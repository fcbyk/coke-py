
cnt = 0
while True:
    fish = input()
    if fish != "$":
        cnt += 1
    if fish == "$":
        break

print("普通鱼的数量是", cnt)
