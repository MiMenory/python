# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример 
# 5 -> 1 2 3 4 5
# 3 -> 1

count_number = int(input('Ввыедите размер массива: '))
list_number = []
count = 1
for i in range(count_number):
    list_number.append(count)
    count += 1
print(list_number)

find_number = int(input('Какую цифру ищем?: '))
numb = 0
for j in range(count_number):
    if list_number[j] == find_number:
        numb += 1
        break
print(f"Число {find_number} встречается {numb} раз")





# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X

# Пример 
# 5 -> 1 2 3 4 5
# 6 -> 5

count_number = int(input('Ввыедите размер массива: '))
list_number = []
count = 1
for i in range(count_number):
    list_number.append(count)
    count += 1
print(list_number)

find_number = int(input('Какое число ищите?: '))
max_number = 0
if find_number > count_number:
    find_number = count_number

for j in range(find_number):
    if list_number[j] > max_number:
        max_number = list_number[j]
print(max_number)




# Домашнее задание
# Задание Пример
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Пример: 
# Ввод: ноутбук
# Вывод: 12


# Заводим словарь. Ключ это баллы. 
list_word = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}


# Приводим все значения в верхний регистр, чтобы исключить опечатки пользователя.
word = input("Введите слово: ").upper()

# цикл
summ = 0
for i in word:
    for k, v in list_word.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")