# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам
# с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

#1 - MY
my_str = 'a a a b c a a d c d d'.split()
count_dict = {}
for letter in my_str:
    if letter in count_dict:
        count_dict[letter] += 1
        print(f'{letter}_{count_dict[letter]}', end=' ')
    else:
        count_dict[letter] = 0
        print(letter, end=' ')
print()

#2
new_list = []
for i in range(len(my_str)):
    letter_count = my_str[:i].count(my_str[i])
    if letter_count > 0:
        new_list.append(f'{my_str[i]}_{letter_count}')
    else:
        new_list.append(my_str[i])
print(*new_list)