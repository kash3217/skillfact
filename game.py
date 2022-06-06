"""Угадай число"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101) # Предлагаемое число
    min = 1 # Минимальное значение
    max = 100 # Максимальное значение

    while True:
        count+=1
        if predict_number > number:
            max = predict_number - 1
            predict_number = (max + min) // 2
        elif predict_number < number:
            min = predict_number + 1
            predict_number = (max + min) // 2
        else:
            break # Выход из цикла если угадал
    return (count)

def score_game(random_predict) -> int:
    """Среднее количeство попыток для угадывания

    Args:
        random_predict (_type_): функция

    Returns:
        int: среднее кол. попыток
    """
    count_ls = []
    np.random.seed(1) #Фиксация сида
    random_array = np.random.randint(1, 101, size=(1000)) # Список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Угадываем число в среднем за: {score} попыток')
    return(score)

#RUN
score_game(random_predict)