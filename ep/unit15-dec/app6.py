year = int(input())
if year % 100 != 0 and year % 4 == 0:
    print("闰年")
elif year % 400 == 0:
    print("闰年")
else:
    print("不是闰年")