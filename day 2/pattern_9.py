# diamond pattern

n = int(input())
# upper half
for i in range(1, n+1):
    # print spaces
    for j in range(n-i):
        print(' ', end='')
    # print stars
    for j in range((2*i)-1):
        print('*', end='')
    print()
n -= 1
# lower half
for i in range(n, 0, -1):
    # print spaces
    spaces = n-i+1
    for j in range(spaces):
        print(' ',end='')
    # print stars
    stars = (2*i)-1
    for j in range(stars):
        print('*', end='')
    print()