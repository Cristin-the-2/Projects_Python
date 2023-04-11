# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – 
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы 
# все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
count1 = count2 = 0
coin = 0
for i in range(n):
    coin = int(input(f"Какой стороной лежит {i+1} монета (0-решка, 1-орел): "))
    if coin == 1:
        count1 += 1
    else:
        count2 += 1
if count1 < count2:
    print(f"Минимальное количество монет которое нужно перевернуть {count1}")
else:
    print(f"Минимальное количество монет которое нужно перевернуть {count2}")