# Семинар 4 (Функции / рекурсия)

# def my_function():
#     pass
# my_function()

# massiv = vvod()
# answer = solve()
# vivod()

# def vvod():
#     pass
# def vivod():
#     pass
# def sole():
#     pass
# def kvadrat(a):
#     return a * a

# n = int(input())
# print(kvadrat(n))


# РЕКУРСИЯ
# 0 1 1 2 3 5 8 13 21
# fib(n) = fib(n -1) + fib(n - 2)
# fib(0) = 0
# fib(0) = 1

# РЯД ФИБОНАЧЧИ

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(7))


#  Варианты реализации циклов

# my_list = []
# n = int(input('Что-то вводим: '))
# for _ in range(n):
#     my_list.append(int(input('еще что-то вводим')))


# #  То же самое одной строкой

# n = int(input('что-то вводим: '))
# string = input('что-то вводим еще: ')
# ist = [int(i) for i in string.split()] # split разобьем и составит список из чисел


# ist = [i for i in range(1, 6) if i % 2 == 0]
# print(ist)



#  ЗАДАЧИ


# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)

# a = [0,1]

# for i in range(50):
#     print(i, fib(i))
# fib(5)
 
# a = [0, 1]
# for i in range(50):
#     a.append(a[-1] + a[-2])
#     print(i, a[-1])





# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# list = [1, 3, 3, 3, 4, 4]
# min_lst = min(list)
# max_lst = max(list)
# new_lst = []
# for i in list:
#     if i == max_lst:
#         new_lst.append(min_lst)
#     else:
#         new_lst.append(i)
# print(new_lst)




# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def simple_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
    
a = int(input('Введите число: '))
print(simple_number(a))



# Задача №37. Решение в группах
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

