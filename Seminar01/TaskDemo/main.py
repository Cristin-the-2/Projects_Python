# Вводится два числа, определить большее из них

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print(f"Наибольшее число - {a}")
elif b > a:
    print(f"Наибольшее число - {b}")
else:
    print(f"Числа {a} и {b} равны.")

# print(f"Наибольшее число: {max(int(input('Введите первое число: ')), int(input('Введите второе число: ')))}")
