import math
s = input()
k = 0
for i in range(math.floor(len(s)/2)):
    if s[i] == s[-(i+1)]:
        k = 0
    else:
        k = 1
if k == 0:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

