n = int(input())

for i in range(1, n+1):
    # print spaces
    spaces = n-i
    for j in range(spaces):
        print(' ', end='')
    # print stars
    stars = i
    stars *= 2
    stars -= 1
    for j in range(stars):
        print('*', end='')
    print()