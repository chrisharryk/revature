# inverted right angle triangle - right alinged

n = int(input())
for i in range(n, 0, -1):
    spaces = n - i
    for j in range(spaces):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()