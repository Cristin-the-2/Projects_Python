# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга 
# оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

#1
num = int(input('Введите число: '))
max_num = num
while num != 0:
    num = int(input('Введите число: '))
    if num > max_num: max_num = num
print(f'Значение наибольшего элемента последовательности {max_num}.')

#2
my_list = []
number = None
while number != 0:
    number = int(input('Введите число: '))
    my_list.append(number)
print(max(my_list))

#3 - маржовый оператор - запрашивать значение переменной в условии
my_list = []
while (number:= int(input('Введите число: '))) != 0:
    my_list.append(number)
print(max(my_list))

# Ваня:
# n = int(input())
# max_number = 1000     - надо минимальное значение
# while n != 0:
#   n = int(input())
#   if max_number > n:  - надо знак наоборот
#       max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
#  while n < 0:         - надо не равно
#   n = int(input())
#   if max_number < n:
#       n = max_number  - надо максимум = н
# print(n)              - надо печатать максимум