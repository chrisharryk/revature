# swap 2 nums without a 3rd variable

a, b = map(int, input().split())
a = a + b
b = a - b
a = a - b
print(a, b)