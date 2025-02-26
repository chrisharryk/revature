# make a list of even numbers from 1 - 10 using comprehension

A = []
for i in range(1, 11):
    if i % 2 == 0:
        A.append(i)
print(A)

A.clear()
A = [i for i in range(1, 11) if i % 2 == 0]
print(A)