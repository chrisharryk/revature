# finding the closest number to zero in the list

A = list(map(int, input().split()))
ans = float('inf')
for x in A:
    if abs(x) < ans:
        ans = x
print(ans)