

def ask_move(player, board):
    # дать игроку возможность сделать ход, то есто есть ввести координаты
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y) 
    # задать условие, которое проверяет, свободно ли место
    if (0 < x < 2) and (0 < y < 2) and (board[x][y] == " "):
        # если клетка свободна, вернуть её координаты
        return (x, y)
    else:
        print("Клетка занята. Введите координаты еще раз.")
        return ask_move(player, board)


def make_move(player, board, x, y):
    # проверить, что клетка свободна
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    # если клетка свободна, записать ход
    board[x][y] = player
    return True


def ask_and_make_move(player, board, x, y):
    x, y = ask_move(player, board, x, y)
    # координаты x, y взять из функции ask_move(player, board)
    make_move(player, board, x, y)