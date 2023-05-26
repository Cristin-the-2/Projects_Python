# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
# находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os
import shutil
import Functions

os.chdir('C:/Users/User/Desktop/Cristin_GB/Projects_Python/Seminar08')

Functions.info_func()
while (user_action:=int(input('Выберите действие (1,2,3 и т.д.): '))) != 6:
    match user_action:
        case 1: Functions.print_records()
        case 2: Functions.add_record()
        case 3: Functions.find_record()
        case 4: Functions.change_record()
        case 5: Functions.delete_record()
        case 6: pass
        case _: print('Нет такого действия.')
