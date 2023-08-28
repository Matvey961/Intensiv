import random
a = []
n = random.randint(1,10)
for i in range (n):
    a.append(random.randint(1,10))
print(a)

b = a[::-1]
print(b)

print('Длина списка: ', len(a))
print('Последний элемент списка: ',a[-1])
if 55 in a and 1717 in a:
    print('Yes')
else:
    print('No')
del a[-1]
del a[0]
print('Список с удаленным первым и последним элементом:', a)

