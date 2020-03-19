game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_matrix(game_map, player=0, row=0, column=0, display=False):
    try:
        print('   0  1  2')
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    
    except IndexError as e:
        print('Error: make sure you input row/column within 0 1 or 2?', e)

    except Exception as e:
        print('Something went very wrong!', e)


game = game_matrix(game, display=True)
print()

game = game_matrix(game, player=1, row=2, column=1)