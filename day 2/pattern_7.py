# pyramid

n = int(input())
for i in range(1, n+1):
    # print spaces
    spaces = n-i
    for j in range(spaces): print(' ', end='')
    # print stars
    stars = i
    for j in range(stars): print('*', end='')
    for j in range(stars-1): print('*',end='')
    print()