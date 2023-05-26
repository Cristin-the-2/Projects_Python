import os
import shutil

def info_func():
    print('[1] Показать все записи.')
    print('[2] Добавить новую запись.')
    print('[3] Найти запись.')
    print('[4] Изменить запись.')
    print('[5] Удалить запись.')
    print('[6] Выход.')

def print_records():
    with open('Task49.txt', 'r', encoding='utf-8') as f:
        print('\nВсе имеющиеся записи:')
        for line in f:
            print(line.strip())
        print()
    info_func()

def add_record():
    with open('Task49.txt', 'a', encoding='utf-8') as f:
        f.write(input('Введите фамилию, имя, телефон: '))
        f.write('\n')
        print('Данные успешно сохранены!')
        print()
    info_func()

def find_record():
    with open('Task49.txt', 'r', encoding='utf-8') as f:
        search = input('Введите искомую запись: ')
        for line in f:
            if search in line:
                print('\nИскомая запись:')
                print(line.strip())
                print()
    info_func()

def change_record():
    with open ('Task49.txt', 'r', encoding='utf-8') as infile, open ('Task49_temp.txt', 'w', encoding='utf-8') as outfile:
        search = input('Введите искомую для изменения запись: ')
        for line in infile:
            if search not in line:
                outfile.write(line)
            else:
                outfile.write(input('Введите новые данные: '))
                outfile.write('\n')
                print('Данные успешно сохранены!')
    os.remove('Task49.txt')
    os.rename('Task49_temp.txt', 'Task49.txt')
    info_func()

def delete_record():
    with open ('Task49.txt', 'r', encoding='utf-8') as infile, open ('Task49_temp.txt', 'w', encoding='utf-8') as outfile:
        search = input('Введите искомую для удаления запись: ')
        for line in infile:
            if search not in line:
                outfile.write(line)
    os.remove('Task49.txt')
    os.rename('Task49_temp.txt', 'Task49.txt')
    info_func()