game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def game_board():
    print('   1  2  3')
    for count, row in enumerate(game, start=1):
        print(count, row)


board = game_board

board()

game[0][0] = 1
board()

game[0][1] = 2
board()

game[0][2] = 3
board()
