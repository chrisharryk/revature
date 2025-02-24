# remove duplicates from list and return it to user

A = list(map(int, input().split()))
n = len(A)
seen = set()
ans = []
for x in A:
    if x not in seen:
        ans.append(x)
        seen.add(x)
print(ans)