#  ДЗ 4 семинара



# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


count_number1 = int(input('Введите кол-во элементов 1-ого списка: '))
count_number2 = int(input('Введите кол-во элементов 2-ого списка: '))

num1 = []
for i in range(count_number1):
    add_numb = int(input('Вводите число 1 множества: '))
    num1.append(add_numb)

num2 = []
for i in range(count_number2):
    add_numb = int(input('Вводите числа 2 множества: '))
    num2.append(add_numb)

print('Проверяем что получилось: ')
print(num1)
print(num2)


# Теперь надо пробежаться по каждому списку.


for j in range(len(num1)):
    inx = j
    for l in range(j + 1, len(num1)):
        if num1[l] < num1[inx]:
            index = l
            num1[j], num1[index] = num1[index], num1[j]
print(num1)

for j in range(len(num2)):
    inx = j
    for l in range(j + 1, len(num2)):
        if num2[l] < num2[inx]:
            index = l
            num2[j], num2[index] = num2[index], num2[j]
print(num2)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.