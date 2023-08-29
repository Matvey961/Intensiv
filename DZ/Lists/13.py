g = list(map(int, input().split()))
print(g)
max = max(g)
min = min(g)
a = []
for i in range(len(g)):
    if g[i] == min:
        a.append(max)
    elif g[i] == max:
        a.append(min)
    else:
        a.append(g[i])
print(a)