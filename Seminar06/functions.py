def create_arr(arr_numb=''):
    my_arr = []
    for i in range(int(input(f'Введите длину {arr_numb} массива: '))):
        my_arr.append(int(input(f'Введите {i+1} элемент {arr_numb} массива: ')))
    return my_arr

def find_same(arr_1, arr_2):
    arr_same = []
    for elem in arr_1:
        if elem not in arr_2: arr_same.append(elem)
    return arr_same

def count_biggest(arr):
    count = 0
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]: count +=1
    return count

def count_same(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] in arr[:i]: count +=1
    return count

def find_sum_divider(number):
    sum_divider = 0
    for divider in range(1, (number // 2) + 1):
        if number % divider == 0: sum_divider += divider
    return sum_divider