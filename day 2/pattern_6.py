# hollow rectangle

n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        for j in range(n): print('*',end='')
    else:
        for j in range(n):
            if j == 0 or j == n-1:
                print('*',end='')
            else:
                print(' ', end='')
    print()