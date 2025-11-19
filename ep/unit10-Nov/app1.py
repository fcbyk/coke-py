a = input()
print(type(a))

a = a.split()
print(a)
print(type(a))

b = list(map(int,a))
print(b)

print(sum(b))