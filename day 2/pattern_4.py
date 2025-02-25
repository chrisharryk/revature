# right angled triangle - right aligned

n = int(input())
for i in range(1, n+1):
    # print spaces
    spaces = n - i
    for j in range(spaces): print(' ', end=' ')
    # print stars
    stars = n - spaces
    for j in range(stars): print('*', end=' ')
    print()