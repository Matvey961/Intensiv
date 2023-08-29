s = input()
a = s.split(sep=' ')
b = []
n = len(a)
for i in range(n):
    b.append(min(a))
    a.remove(min(a))
print(b)