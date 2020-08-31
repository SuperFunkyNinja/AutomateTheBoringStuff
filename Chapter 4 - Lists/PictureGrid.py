import random

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        print(grid[x][y],end='')
    print()
    # print('

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in spam:

    if spam.index(i) != len(spam) - 1:
        print(i, end='')
        print(', ',end='')

    if spam.index(i) == len(spam) - 1:
        print('and ',end='')
        print(i)

numberOfStreaks = 0

for experimentNumber in range(10000):
    set = []
    for i in range(100):
        set.append(random.randint(0,1))

    if '1, 1, 1, 1, 1, 1, 1, 1, 1, 1' in str(set):
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

