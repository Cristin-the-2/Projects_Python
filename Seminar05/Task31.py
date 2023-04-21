# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

import functions

n = int(input('Введите номер необходимого числа: '))
print(f'Число Фибоначчи под номером {n} : {functions.fibonacci(n)}.')