### parameter type을 설정할수있는 방법 => cython
### 실제로 쓰이는 경우가 거의 없기는 함

'''
def addition(x, y):
    return x + y

z = addition('hey ', 'there')
print(z)
'''

game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def game_board(player=0, row=0, column=0, just_display=False):
    print('   0  1  2')
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board()
print()

game_board(player='x', row=2, column=1)

