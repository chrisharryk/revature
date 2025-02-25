# remove duplicates from list and return it to user

A = list(map(int, input().split()))
n = len(A)
seen = set()
distinct = []
dupes = set()
for x in A:
    if x not in seen:
        distinct.append(x)
        seen.add(x)
    else:
        dupes.add(x)
print(distinct, dupes)