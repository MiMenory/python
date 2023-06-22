# Коллекции данных. Профилирование и отладка

list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]
print(*list_1) # если мы ставим * это значит что мы убираем скобочки и раскрываем значения внутри

for i in list_1:
    print(i)
 
print(len(list_1))
print(list_1[3])

# добавить значение в список

list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
list_1.append(85)
print(list_1)

list_2 = []
for i in range(5):
    list_2.append(i)
    print(list_2)


#  удаленение значения из списка

list_3 = [12, 7, -1, 21, 0]
print(list_3.pop()) # 0
print(list_3) # 12 7 -1 21
print(list_3.pop()) # 21
print(list_3) # 12 7 -1
print(list_3.pop(0)) # 21
print(list_3) # 7 -1
# и т.д.

# добавление элемента на нужную позицию
list_3 = [12, 7, -1, 21, 0]
print(list_3)
print(list_3.insert(2, 11))
print(list_3)


