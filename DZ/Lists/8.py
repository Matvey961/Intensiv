n = int(input())
a = []
b =[]
for i in range(n):
    k = int(input())
    a.append(k)
print(a)
for i in range(n):
    if i % 2 != 0:
        del a[i]
print(a)
