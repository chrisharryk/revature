# find the second highest element in the list

A = list(map(int, input().split()))
mx = max(A)
ans = float('-inf')
for x in A:
    if x < mx and x > ans:
        ans = x
print(ans)