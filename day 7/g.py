from collections import Counter

text = "Hello, hello! How are you? Are you doing well?"
extras = '?', '!', ','

ans = {}
for x in text.split(' '):
    if x[-1] in extras:
        if x[:-1] in ans:
            ans[x[:-1]] += 1
        else:
            ans[x[:-1]] = 1
    else:
        if x in ans:
            ans[x] += 1
        else:
            ans[x] = 1

print(ans)