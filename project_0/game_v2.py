"""Игра угадывает число
Число загадывает и угадывает сам компьютер"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадывает число

    Аргументы:
        number (int, optional): Загаданное число. По умолчанию 1.

    Возвращает:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        
        predict_number = np.random.randint(1, 101)
        
        if predict_number == number:
            break
        
    return count

def binary_predict(random_number: int=1) -> int:
    """Угадывает число при помощи алгоритма бинарного поиска

    Аргумент:
        random_number (int): загаданное число. По умолчанию 1

    Возвращает:
        int: Число попыток 
    """
    # Диапазон поиска
    find_range = [0, 101]
    
    # Первое предсказанное значение - середина
    predicted_number = int(sum(find_range) / 2)
    
    # Счетчик
    count = 0
    
    while True:
        count += 1
        
        if check_number(random_number, predicted_number) < 0:
            # Загаданное число меньше-правая граница диапазона = predicted_num
            find_range[1] = predicted_number
            
            # Предсказанное значение берется из середины диапазона 
            # Округляется в меньшую сторону
            predicted_number = int(sum(find_range) / 2)
        
        elif check_number(random_number, predicted_number) > 0:
            # Загаданное число больше-левая граница диапазона = predicted_num
            find_range[0] = predicted_number
            
            # Предсказанное значение берется из середины диапазона 
            # Округляется в большую сторону-для random_number=100-сокращает
            # поиск на 1 попытку
            predicted_number = round(sum(find_range) / 2)
            
        else:
            # Если числа равны - возврат числа попыток
            return count

def check_number(random_num: int, predict_num: int) -> int:
    """Проверяет равенство загаданного и предсказанного чисел

    Аргументы:
        random_num (int): загаданное число
        predict_num (int): предсказанное число

    Возвращает:
        int: -1 - если загаданное число меньше предсказанного
              1 - если загаданное число больше предсказанного
              0 - если числа равны
    """
    if random_num < predict_num:
        return -1
    elif random_num > predict_num:
        return 1
    else:
        return 0    

def score_game(random_predict) -> int:
    """Среднее число попыток. 1000 случаев

    Аргументы:
        random_predict ([type]): Функция, которая угадывает число

    Возвращает:
        int: среднее число попыток
    """
    count_ls = []
    # Вариант случайного массива не фиксируется - иначе будет один 
    # и тот же результат
    # np.random.seed(1) 
    # Список случайных чисел
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    # Среднее число попыток
    score = int(np.mean(count_ls))
    print(f'Среднее число попыток: {score}')

    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_predict)
