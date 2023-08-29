a = [1, 2, 34, 6, 2, 2]
print(a)
#print(type(a))
#print(len(a))
#print(sum(a))

#print(b)
#b = a[:-2] # Срез
#print(b)
b = [3, 5, 7, 54]
#print(a+b) #Сложение
a.extend(b)
print(a)

t = a.pop(2) #Удаляет элемент с индексом 2 и возвращает его
print(t)
print(a)

del a[-1] #Удаляет элемент с индексом -1
print(a)

#a.clear()#Очищает список

#a.insert(0,111)
#print(a)

#a.index(4) #Возвращает индекс первого элемента со значением 4

#print(a.remove(7)) #Удаляет первую 7

#print(a.count(2)) #Количество двоек

#a.reverse() #Переворачивает список
#print(a)

#a.sort() #Сортирует по возрастанию

#for i in range(len(a)):
    #print(a[i],end = "")
#for x in a:
    #print(x)

#print("")

#print(*a) #Еще один вывод списка

#g = list(map(int, input().split())) #Считывает список map() применяет int() к каждому элементу списка, list[] переводит в список
#Split превращает строку в список
print(g)

#d = ['f', 'e', 'i']
#print(' ',join(d))



