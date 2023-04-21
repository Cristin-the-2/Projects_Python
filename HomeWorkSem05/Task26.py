# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(num, deg):
    if deg == 1: return num
    else: return num * exponentiation(num, deg-1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(f'Число {a} в степени {b} равно {exponentiation(a,b)}')