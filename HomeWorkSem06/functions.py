def int_input(text):
    return int(input(text))

def arith_progr(a1, d, n):
    progr_list = []
    for a in range(1,n+1):
        progr_list.append(a1 + d*(a-1))
    return progr_list

def create_list():
    result_list = []
    for i in range(int(input(f'Введите длину списка: '))):
        result_list.append(int(input(f'Введите {i+1} элемент списка: ')))
    return result_list

def find_index(some_list, some_min, some_max):
    result_list = []
    for i in range(len(some_list)):
        if some_min < some_list[i] < some_max: result_list.append(i)
    return result_list