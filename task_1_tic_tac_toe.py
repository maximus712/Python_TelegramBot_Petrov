


board = [[" " for i in range(3)] for j in range(3)]
player = "X"

def draw_board(board):  
    # запустить цикл, который проходит по всем 3 строкам доски
    for i in range(3):
        # поставить разделители значений в строке 
        print(" | ".join(board[i]))
        # поставить разделители строк 
        print("---------")


def ask_move(player, board):
    # дать игроку возможность сделать ход, то есто есть ввести координаты
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y) 
    # задать условие, которое проверяет, свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
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


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    # координаты x, y взять из функции ask_move(player, board)
    make_move(player, board, x, y)


def check_win(player, board):
    # проверить, совпадают ли значения в строках и столбцах
    for i in range(3):
        # проверить, совпадают ли значения в строках
        if board[i] == [player, player, player]:
            return True
        # проверить, совпадают ли значения в столбцах
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # проверить, совпадают ли значения на диагонали из верхнего левого в нижний правый угол
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # проверить, совпадают ли значения на диагонали из верхнего правого в нижний левый угол
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def tic_tac_toe():
    # задать бесконечненый цикл, который проводит игры
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        # задать бесконечнный цикл, который проводит конкретную игру
        while True:
            # нарисовать игровое поле
            draw_board(board)
            # запросить ход
            ask_and_make_move(player, board)
            # проверить, выиграл ли игрок
            if check_win(player, board):
                print(f"{player} выиграли!")
                break
            # проверить, произошла ли ничья
            tie_game = True
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = False
            # если произошла ничья, завершить цикл
            if tie_game:
                break
            player = "O" if player == "X" else "X"
        # спросить игроков, хотят ли они сыграть еще нраз
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break


if __name__ == "__main__":
    tic_tac_toe()

        