# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы

scrabble_eng = {1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'], 
                2: ['d', 'g'],
                3: ['b', 'c', 'm', 'p'], 
                4: ['f', 'h', 'v', 'w', 'y'], 
                5: ['k'],
                8: ['j', 'x'], 
                10: ['q', 'z']}

scrabble_rus = {1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], 
                2: ['д', 'к', 'л', 'м', 'п', 'у'], 
                3: ['б', 'г', 'ё', 'ь', 'я'], 
                4: ['й', 'ы'], 
                5: ['ж', 'з', 'х', 'ц', 'ч'], 
                8: ['ш', 'э', 'ю'], 
                10: ['ф', 'щ', 'ъ']}

word = input('Введите слово: ').lower()
count = 0

for key, val in scrabble_rus.items():
    for i in range(len(val)):
        for j in range(len(word)):
            if val[i] == word[j]:
                count += key

for key, val in scrabble_eng.items():
    for i in range(len(val)):
        for j in range(len(word)):
            if val[i] == word[j]:
                count += key

print(f'Стоимость введенного слова {count} очков.')