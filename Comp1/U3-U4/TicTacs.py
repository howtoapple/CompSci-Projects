import numpy as np

def create_board():
    return (np.array([0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))


    def coordinates(board, player):
        i, j, cn = (-1, -1, 0)
        while (i > 3 or i < 0 or j < 0 or j > 3) or (board[i][j] != 0):
            if cn > 0:
                print("Wrong Input! Try Again")
            print("Player {}'s turn".format(player))
            i = int(input("x-coordinates: "))
            j = int(input("y-coordinates: "))
            i = i - 1
            j = j - 1
            cn = cn + 1
        board[i][j] = player
        return board


    def row_win(board, player):
        for row in board:
            if all([cell == player for cell in row]):
                return True
        return False

    def col_win(board, player):
        for x in range(len(board)):
            win = True

            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue

        return win


    def diag_win(board, player):
        win = True
        y = 0
        for x in range(len(board)):
            if board[x][x] != player:
                win = False
        if win:
            return win
        win = True
        if win:
            for x in range(len(board)):
                y = len(board) - 1 - x
                if board[x][y] != player:
                    win = False
        return win


    def evaluate(board):
        winner = 0

        for player in [1, 2]:
            if (row_win(board, player) or
                    col_win(board, player) or
                    diag_win(board, player)):
                winner = player

        if np.all(board != 0) and winner == 0:
            winner = -1
        return winner


    def play_game():
        board, winner, counter = create_board(), 0, 1
        print(board)
        while winner == 0:
            for player in [1, 2]:
                board = coordinates(board, player)
                print("Board after " + str(counter) + " move")
                print(board)
                counter += 1
                winner = evaluate(board)
                if winner != 0:
                    break
        return winner

    print("Winner is: " + str(play_game()))