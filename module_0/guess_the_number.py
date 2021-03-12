import numpy as np


def game_core_v3(number):
    ''' Сначала устанавливаем середину интервала, а затем выбираем середину интервала,
        в который попадает число по результатам сравнения.
        Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 51
    top = 101
    bottom = 0
    while number != predict:
        count += 1
        if number > predict:
            bottom = predict
            predict += (top - predict) // 2
        elif number < predict:
            top = predict
            predict -= (predict - bottom) // 2

    return count  # выход из цикла, если угадали


def score_game(game_core):
    ''' Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число '''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)

