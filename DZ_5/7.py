n = int(input())
a = []
b = []
for i in range (n):
    k = int(input())
    b.append(k)
for i in range (n-1):
    a.append(b[i]+b[i+1])
print(a)