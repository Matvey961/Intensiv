s = input()
p = ['txt', 'pdf', 'txt']
for i in range(len(s)):
    if s[i] == '.':
        r = s[i+1:]
if r in p:
    print('Good!')
else:
    print('Bad!!!')