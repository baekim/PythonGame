game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_matrix(game_map, player=0, row=0, column=0, display=False):
    print('   0  1  2')
    if not display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    
    return game_map


game = game_matrix(game, display=True)
print()

game = game_matrix(game, player=1, row=2, column=1)

'''
game = 'I want to play a game'
print(id(game))

def game_matrix(player=0, row=0, column=0, display=False):
    # global game
    print(id(game))
    print(game)


game_matrix()
print(game)
print(id(game))
'''

'''
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_matrix(player=0, row=0, column=0, display=False):
    print('   0  1  2')
    if not display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)


game_matrix(display=True)
game_matrix('x', 2, 1)
'''