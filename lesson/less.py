#  Урок 3. Функции, рекурсия, алгоритмы.

# Функция — это фрагмент программы, используемый многократно.
# Мы знакомы уже с функциями с C#, давайте теперь посмотрим, как
# создаются и используются функции внутри Python


def sum_numbers(n): # передали аргумент n
    summa = 0
    for i in range(1, n+1): # так как сумму нужно считать с 1 элемента, по этому 1, n+1
        summa += i
    print(summa)

# вызываем функцию 

sum_numbers(5)

# #  теперь то же самое, чтобы мы возвращаем значения

def sum_numbers(n): # передали аргумент n
    summa = 0
    for i in range(1, n+1): # так как сумму нужно считать с 1 элемента, по этому 1, n+1
        summa += i
    return summa

# # вызываем функцию 

# print(sum_numbers(5))


# #  принимаем неограниченное кол-во агрументов
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str(1,2,3))


import modul as m1
# from modul import * # означает, что мы хотим импортировать все функции
print(m1.max1(10, 9))


# Рекурсия — это функция, вызывающая сама себя.

# С рекурсией Вы знакомы с C#, в Python она ничем не отличается, давай рассмотрим следующую задачу: 
# Пользователь вводит число n. Необходимо вывести n - первых членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих.
# При описании рекурсии важно указать, когда функции надо остановиться и
# перестать вызывать саму себя. По-другому говоря, необходимо указать базис рекурсии

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)



#  Задача, угадать число от 0 до 100
#  загадали число 77

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([10, 5, 2, 3]))


#  разбор рекурсии 


# Быстрая сортировка
# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2, 3]
# ○ pivot = 10
# ○ less = [5, 2, 3]
# ○ greater = []
# ○ return quicksort([5, 2, 3]) + [10] + quicksort([])

# ● 2-е повторение рекурсии:
# ○ array = [5, 2, 3]
# ○ pivot = 5
# ○ less = [2, 3]
# ○ greater = []
# ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии
# добавляется список [10]

# ● 3-е повторение рекурсии:
# ○ array = [2, 3]
# ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: [2, 3] + [5] + [10] = [2, 3, 5,
# 10]




#  сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)


