# leetcode - good pairs, my solution

A = list(map(int, input().split()))
n = len(A)
ans = 0
for i in range(n-1):
    for j in range(n):
        if i < j and A[i] == A[j]: ans += 1
print(ans)