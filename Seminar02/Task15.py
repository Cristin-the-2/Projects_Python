# Пользователь вводит число N - количество арбузов. 
# Найти самый легкий и самый тяжелый арбуз.

N = int(input('Введите количество арбузов: '))
max_w = 0
min_w = 30

for i in range(1, N+1):
    weight = int(input(f'Введите вес {i} арбуза: '))
    if weight > max_w: max_w = weight
    elif weight < min_w: min_w = weight
print(f'Самый маленький арбуз весит {min_w} , а самый большой весит {max_w}.')