# inverted pyramid

n = int(input())
for i in range(n, 0, -1):
    # print spaces
    spaces = n-i
    for j in range(spaces):
        print(' ',end='')
    # print stars
    stars = (2*i)-1
    for j in range(stars):
        print('*', end='')
    print()