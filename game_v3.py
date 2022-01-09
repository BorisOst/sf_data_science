"""Игра угадывает число
Число загадывает и угадывает сам компьютер"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадывает число

    Загаданное число:
        number (int, optional): [description]. По-умолчанию равно 1.

    Возвращает количество попыток:
        int: [description]
    """
    
    count = 0
    
    while True:
        count += 1
        
        predict_number = np.random.randint(1, 501)
        
        if predict_number == number:
            break
        
    return count

def score_game(random_predict) -> int:
    """[summary]

    Args:
        random_predict ([type]): [description]

    Returns:
        int: [description]
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Среднее число попыток: {score}')

    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
