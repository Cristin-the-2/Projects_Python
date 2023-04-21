def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (fibonacci(n - 1) + fibonacci(n - 2))

def change_score(score_list):
    for i in range(len(score_list)):
        if score_list[i] == max(score_list):
            score_list[i] = min(score_list)
    return score_list

def simple_number(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'No'
    return 'Yes'

def rec_print(len_n):
    num = input('Введите число: ')
    if len_n == 1: return num
    return rec_print(len_n-1) + ' ' + num