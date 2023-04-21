# Задача 1
# Есть список 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5.
# print(*list(filter(lambda elem: elem < 5, a_1)))
# print([elem for elem in a_1 if elem < 5])

# Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# print(set(a_2).intersection(set(b_2)))
# print(list(filter(lambda elem: elem in b_2, a_2)))
# print([elem for elem in a_2 if elem in b_2])

# Задача 3 (!!!!!)
# Отсортируйте словарь по значению в порядке возрастания и убывания.
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(dict(sorted(d.items(), key=operator.itemgetter(1))))
# print(dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)))

# Задача 4
# Напишите программу для слияния нескольких словарей в один.
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# result = dict()
# for d in (dict_a, dict_b, dict_c):        (!!!) не работает
#     result.update[d]
# result = {**dict_a, **dict_b, **dict_c}
# print(result)

# Задача 5
# Найдите три ключа с самыми высокими значениями в словаре 
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# import operator
# result = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
# print(list(result)[:3])
# from heapq import nlargest
# result = nlargest(3, my_dict, key=my_dict.get)  (!!!) не работает

# Задача 6
# Напишите код, который переводит целое число в строку, при том что его можно 
# применить в любой системе счисления.
# print(int('ABC', 16))
# print(int('1001001', 2))

# Задача 7
# Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине 
# и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных 
# над ним чисел.

# def pascal_triangle(n):
#    row = [1]
#    y = [0]
#    for x in range(max(n, 0)):
#       print(row)
#       row = [left + right for left, right in zip(row + y, y + row)]
# pascal_triangle(6)

# Задача 8
# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово 
# или фраза, которые одинаково читаются слева направо и справа налево.
# my_str = input('-->')
# reversed_str = my_str[::-1]
# if my_str == reversed_str: print('YES')
# else: print('NO')

# Задача 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# def convert(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
# convert(123456)

# Задача 10
# Вы принимаете от пользователя последовательность чисел, разделённых запятой. 
# Составьте список и кортеж с этими числами.