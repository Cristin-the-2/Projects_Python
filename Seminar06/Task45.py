# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых 
# не превосходит k. Программа получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все пары дружественных чисел, 
# каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз 
# (перестановка чисел новую пару не дает).

# 1 - MY
# k = int(input('Введите число не превосходящее 10^5: '))

# if k <= 10**5:
#     res_list = []
#     for n in range(2,k):
#         my_sum = 0
#         for divider in range(1,n):
#             if n % divider == 0: my_sum += divider
#         if (my_sum <= k)&(my_sum != n):
#             m = my_sum
#             my_sum = 0
#             for divider in range(1,m):
#                 if m % divider == 0: my_sum += divider
#             if my_sum == n: 
#                 res_list.append(n)
#                 res_list.append(m)
#     for i in range(0, len(res_list), 2):
#         if res_list[i] not in res_list[:i]: print(f'{res_list[i]} {res_list[i+1]}')
# else: print('Введено не верное значение.')

# 2
import functions

k = int(input('Введите число не превосходящее 10^5: '))

for n in range(2, k):
    m = functions.find_sum_divider(n)
    if n == functions.find_sum_divider(m) and n != m and n < m:
        print(n, m)