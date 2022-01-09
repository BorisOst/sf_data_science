"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    test_number = int(input('Введите число от 1 до 100: '))
    
    count += 1
    
    if test_number > number:
        print(f'Попытка {count}. Число должно быть меньше')
    elif test_number < number:
        print(f'Попытка {count}. Число должно быть больше')
    else:
        print(f'Вы угадали число за {count} попыток. Оно равно: {number}')
        break
    