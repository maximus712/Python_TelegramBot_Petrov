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