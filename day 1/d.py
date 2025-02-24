# dictionary contains names as keys and scores as values.
# Return the name and score of the highest scorer.

n = int(input())
mp = {}
ans = ['x', float('-inf')]
for _ in range(n):
    name, score = input().split()
    mp[name] = int(score)
    if mp[name] > ans[1]:
        ans[0] = name
        ans[1] = int(score)
print(f'student {ans[0]} has the highest score of {ans[1]}')