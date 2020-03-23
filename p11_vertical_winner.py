game = [[2, 0, 1],
        [1, 0, 0],
        [2, 2, 1],]


# instead of, columns = [0,1,2]
# columns = list(range(3))
# print(columns)

for col in range(len(game)):
    check = []
    
    for row in game:
        check.append(row[col])
        
    if check.count(check[col]) == len(check) and check[0] != 0:
        
        print('Winner!')

'''
def win(current_game):
    for row in game:
        print(row)
        
        # row[0]이 row의 [다른항목]과 같을경우 'winner', #0일 경우는 제외
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner')


win(game)
'''