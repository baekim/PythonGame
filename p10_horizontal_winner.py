game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0], ]


def win(current_game):
    for row in game:
        print(row)
        
        # row[0]이 row의 [다른항목]과 같을경우 'winner', #0일 경우는 제외
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner')


win(game)