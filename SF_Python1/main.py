# SkillFactory Data Science Unit0 Final test
# Крестики-нолики
global data


def greeting():
    # just greetings
    hellowords = '''
    ----------------
    xx   xx    xx
     xx xx   xx  xx
      xxx    xx  xx
     xx xx   xx  xx
    xx   xx    xx
    ----------------    
    Hello, adventurer!
    This is an amazing game.
    Just try.
    '''
    print(hellowords)

def draw_field(data):
    # draw field with boundaries
    print()
    for row in data:
        print('', end='|')
        for val in row:
            print(val, end='|')
        print()
    print()


def check_input(input_data):
    # check input for correct format: two spaced integers [0-2]
    global data
    input_array = input_data.split()
    if len(input_array) != 2:
        print('Введите две координаты через пробел!')
        print('Пример: 1 1')
        return False
    elif not input_array[0].isdigit() or not input_array[1].isdigit():
        print('Введите числа!')
        print('Пример: 1 1')
        return False
    elif 0 < int(input_array[0]) > 2 or 0 < int(input_array[1]) > 2:
        print('Введите числа в диапазоне 0 - 2!')
        print('Пример: 2 0')
        return False
    elif data[int(input_array[0])][int(input_array[1])] != '-':
        print('Поле занято!')
        return False
    else:
        return [int(s) for s in input_array]


def make_turn():
    # get, check and return correct user data
    while True:
        input_data = input('Введите координаты: ')
        res = check_input(input_data)
        if res:
            return res
        else:
            continue

def check_win(player):
    # check all win conditions
    win1 = True
    win2 = True
    for i in range(3):
        win3 = True
        win4 = True
        win1 = win1 and data[i][i] == player
        win2 = win2 and data[2 - i][i] == player
        for j in range(3):
            win3 = win3 and data[i][j] == player
            win4 = win4 and data[j][i] == player
        if win3 or win4:
            draw_field(data)
            return True

    if win1 or win2:
        draw_field(data)
        return True

def play():
    # main algorithm
    greeting()
    turn = 1
    row = ["-"] * 3
    global data
    data = [row.copy() for _ in range(3)]
    draw_field(data)
    while True:
        player = 'o' if turn % 2 == 0 else 'x'
        if turn <= 9:
            print('Ход %s' % player)
            coords = make_turn()
            data[coords[0]][coords[1]] = player
            if check_win(player):
                print('\n--------------------')
                print('Победа %s!' % player)
                break
            draw_field(data)
            turn += 1
        else:
            print('\n--------------------')
            print('Ничья!')
            break


play()
