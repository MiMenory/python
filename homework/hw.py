#  Варианты реализации циклов

my_list = []
n = int(input('Что-то вводим: '))
for _ in range(n):
    my_list.append(int(input('еще что-то вводим')))


#  То же самое одной строкой

n = int(input('что-то вводим: '))
string = input('что-то вводим еще: ')

ist = [int(i) for i in string.split()]