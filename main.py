from typing import List, Any

"""
Функция, инициализурющая игровое поле, 
которое предстаялет собой матрицу
рамерности NxN
"""
def game_field_init(s: int) -> List[List]:
    return [[None for j in range(s)] for i in range(s)]


"""
Функция, проверяющая является ли строка выигрышной.
По сути берется сэт от списка(горизонтали, вертикали, диагонали матрицы)
и если там только один элемент и он не None, то победа
"""
def is_winning_line(l: list) -> str:
    l_set = set(l)
    if len(l_set) == 1 and list(l_set)[0] is not None:
        print(f'{list(l_set)[0]} победили')
        return True


"""
Функция, проверяющая закончилась ли игра.
Проверка горизонталей, вертикалей и диагоналей поля.
Также проверяется, остались ли свободные ячейки на поле
"""
def check_if_game_end(m: List[List]) -> bool:
    for l in m:
        if is_winning_line(l):
            return True

    for l in zip(*m):
        if is_winning_line(l):
            return True

    p = []
    s = []
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if i == j:
                p.append(m[i][j])
            if (i + j) == (len(m) - 1):
                s.append(m[i][j])


    if is_winning_line(p):
        return True
    if is_winning_line(s):
        return True

    if not any(None in sub for sub in m):
        print("Ничья! На поле больше не осталось свободных ячеек")
        return True

    return False


"""
Функция отображения игрового поля
"""
def display_field(m: List[List]) -> None:
    horizontal_ind = ' | '.join([str(j) for j in range(2, len(m) + 1)])
    print('  1 | ' + horizontal_ind)
    j = 1
    for i in m:
        st = ' | '.join([j if j else ' ' for j in i])
        vertical_ind = str(j)
        j += 1
        print(f'{vertical_ind} {st}')


"""
Функция, проверяющая являются введеные координаты валидными.
Соответствуют размерности игрового поля, занята ли ячейка и т.п.
"""
def valid_input(s1: Any, s2: Any, m: List[List]) -> bool:
    try:
        (1 <= int(s1) <= len(m)) or (1 <= int(s2) <= len(m))
        if m[int(s2) - 1][int(s1) - 1] is not None:
            print("Ячейка уже занята! Попробуйте другие координаты")
            return False
        return True
    except:
        print(f"Одна или обе координаты некорректны, попробуйте значения от 1 до {len(m)}")
        return False


"""
Функция, отвечающая за ввод координат при совершении хода игроком
"""
def player_input(p: int):
    x = input(f"Игрок {p}. Введите координату по горизонтали: ")
    y = input(f"Игрок {p}. Введите координату по вертикали: ")
    while not valid_input(x, y, game_field):
        x = input(f"Игрок {p}. Введите координату по горизонтали: ")
        y = input(f"Игрок {p}. Введите координату по вертикали: ")

    if p == 1:
        game_field[int(y) - 1][int(x) - 1] = 'X'
    elif p == 2:
        game_field[int(y) - 1][int(x) - 1] = 'O'

    display_field(game_field)


if __name__ == '__main__':
    n = None
    while n is None:
        input_value = input("Введите размерность поля от 3 до 9: ")
        try:
            if int(input_value) < 3 or int(input_value) > 9:
                n = None
            else:
                n = int(input_value)
        except ValueError:
            print("Вводите только число от 3 до 9!")

    game_field = game_field_init(n)

    go_game = True

    while go_game == True:
        print("Текущее игровое поле")
        display_field(game_field)

        player_input(1)

        if check_if_game_end(game_field):
            go_game = False
            break

        player_input(2)
