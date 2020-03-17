game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

# print(game)
# print()
#
# for row in game:
#     print(row)

print("   1  2  3")
for count, row in enumerate(game, start=1):
    print(count, row)
