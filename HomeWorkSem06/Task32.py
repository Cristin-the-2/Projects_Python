# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

import functions

my_list = functions.create_list()
my_min = functions.int_input('Введите минимальное значение: ')
my_max = functions.int_input('Введите максимальное значение: ')
print(functions.find_index(my_list, my_min, my_max))