# task 4: Sorting Tuples Based on Math Operations

data = [(3, 5), (1, 8), (4, 4), (2, 6)]
data.sort(key=lambda x: (-sum(x), x[0]))
print(data)