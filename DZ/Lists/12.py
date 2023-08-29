import random
a = []
for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
print(a)

#1
del a[1]
a.insert(1,17)
print(a)

#2
a.append([4,5,6])
print(a)

#3
del a[0]
print(a)

#4


