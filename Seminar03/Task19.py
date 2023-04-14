# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю
# последовательность (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers)
numbers1 = [0, 0, 0, 0, 0]

# 1 - MY
for i in range(len(numbers)):
    if i+k > len(numbers)-1:
        numbers1[(k+i) - len(numbers)] = numbers[i]
    else:
        numbers1[k+i] = numbers[i]
print(numbers1)

# 2
for i in range(k):
    # временная переменная  запоминает последнее значение из списка
    tmp = numbers[-1]
    numbers.insert(0, tmp)  # ставим в перую переменную temp
    numbers.pop()  # удаляем последнюю переменную  (по-умолчанию последняя)
print(numbers)

# 3 - BEST
for i in range(k):
    numbers.insert(0, numbers.pop())
print(numbers)

# 4
print(numbers[-k:] + numbers[:-k])