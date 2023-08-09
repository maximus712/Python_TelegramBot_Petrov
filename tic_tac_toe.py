import draw_board, ask_and_make_move,check_win



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
            if not tie_game:
                break
            player = "O" if player == "X" else "X"
        # спросить игроков, хотят ли они сыграть еще нраз
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break