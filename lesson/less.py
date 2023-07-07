# ДЗ 5



# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8




# способ без рекурсии

def fact(a, b):
    a1 = a
    for _ in range(b-1):
        a = a * a1
    return a

# 


def fact(a, b):
    if b == 0:
        return 1
    else:
        return a * fact(a, b - 1)

a = int(input('Введите число: '))
b = int(input('В какую степень возводим?: '))

print(fact(a, b))





# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4


def recursive(a, b,):
    if b == 0:
        return a
    else:
        return recursive(a + 1, b - 1)
    

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))

print(recursive(a, b))


