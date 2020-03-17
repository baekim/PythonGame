# noinspection Pylint
lists = [1, 2, 3, 4, 5]

print(lists[1:])
print(lists[:4])

lists[1] = 99

print(lists)
print(lists[0:2])
print()

game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

game[0][1] = 9

print('   1  2  3')
for count, row in enumerate(game, start=1):
    print(count, row)

