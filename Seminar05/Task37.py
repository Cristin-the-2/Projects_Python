# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

#1 - MY
my_str = input('Введите последовательность чисел: ')
print(my_str[::-1])

#2 - recursion
import functions
n = int(input('Введите длину последовательности: '))
print(functions.rec_print(n))